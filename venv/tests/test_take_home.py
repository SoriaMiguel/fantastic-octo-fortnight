from seeds import seed


def test_show_candidate_list(client):
    response = client.get('/candidate/list')
    # response 200
    # one candidate matches
    # count is correct
    # assert users[1] in response.data

def test_candidate(client):
    response = client.get('/candidate/list')
    # get
    # assert
    # with good candidate_id
    # response 200
    # returns matching candidate
    # includes experience

    # with bad cadndidate id
    # response 200
    # response includes "Could not find candidate: {escape(candidate_id)}"

    # post
    # with good candidate_id
    # response 200
    # returns matching candidate
    # includes experience
