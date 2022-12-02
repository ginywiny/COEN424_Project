from train import *
from data import *
import torch as th
import os

os.environ["CUDA_VISIBLE_DEVICES"]=""

th.cuda.is_available = lambda : False
def infer(user_ratings, top_n):
    args = config()
    dataset = MovieLens(
        args.data_name,
        args.device,
        use_one_hot_fea=args.use_one_hot_fea,
        symm=args.gcn_agg_norm_symm,
        test_ratio=args.data_test_ratio,
        valid_ratio=args.data_valid_ratio,
    )
    # device = th.device('cuda' if th.cuda.is_available() else 'cpu')
    device = th.device('cpu')
    args.src_in_units = dataset.user_feature_shape[1]
    args.dst_in_units = dataset.movie_feature_shape[1]
    args.rating_vals = dataset.possible_rating_values
    net = Net(args=args)
    # net = net.to(args.device)
    net = net.to('cpu')
    net.load_state_dict(th.load("./model.pth", map_location=th.device('cpu')))
    net.eval()
    # nd_possible_rating_values = th.FloatTensor(
    #     dataset.possible_rating_values
    # ).to(args.device)
    nd_possible_rating_values = th.FloatTensor(
        dataset.possible_rating_values
    ).to('cpu')
    # I should create graph with all of the users and movies and get the row of my desired user
    user_rating_movies = list(user_ratings.keys()) #someone like user with id = 1
    user_rating_values = list(user_ratings.values())
    encode_graph_infer = dataset.generate_enc_graph_infer(user_rating_movies, user_rating_values,add_support=True)
    rating_pairs = (np.array([943 for i in range(dataset._num_movie)],
                                 dtype=np.int64),
                        np.array(range(dataset._num_movie), # find rating for these movies
                                 dtype=np.int64))
    decode_graph_infer = dataset.generate_dec_graph_infer(rating_pairs)
    encode_graph_infer = encode_graph_infer.int().to(args.device)
    decode_graph_infer = decode_graph_infer.int().to(args.device)
    infered_ratings = net(
            encode_graph_infer,
            decode_graph_infer,
            None,
            None,
        )

    real_pred_ratings = (
            th.softmax(infered_ratings, dim=1)
            * nd_possible_rating_values.view(1, -1)
        ).sum(dim=1)
    print(th.topk(real_pred_ratings.flatten(), top_n).indices)
    indices = th.topk(real_pred_ratings.flatten(), top_n).indices
    movie_names = []
    for indice in indices:
        movie_names.append(dataset.movie_info["title"][int(indice)])
    print(movie_names)
    return movie_names



def id_to_title(id):
    args = config()
    dataset = MovieLens(
        args.data_name,
        args.device,
        use_one_hot_fea=args.use_one_hot_fea,
        symm=args.gcn_agg_norm_symm,
        test_ratio=args.data_test_ratio,
        valid_ratio=args.data_valid_ratio,
    )
    return dataset.movie_info["title"][int(id)]

def title_to_id(title):
    args = config()
    dataset = MovieLens(
        args.data_name,
        args.device,
        use_one_hot_fea=args.use_one_hot_fea,
        symm=args.gcn_agg_norm_symm,
        test_ratio=args.data_test_ratio,
        valid_ratio=args.data_valid_ratio,
    )
    mylist=list(dataset.movie_info["title"])
    return mylist.index(title)

def list_of_titles():
    args = config()
    dataset = MovieLens(
        args.data_name,
        args.device,
        use_one_hot_fea=args.use_one_hot_fea,
        symm=args.gcn_agg_norm_symm,
        test_ratio=args.data_test_ratio,
        valid_ratio=args.data_valid_ratio,
    )
    return list(dataset.movie_info["title"])


if __name__ == "__main__":
    user_ratings = {1:5,13:5,15:4,16:5}
    infer(user_ratings,6)