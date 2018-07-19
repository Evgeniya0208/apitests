import candidates_api
import json

def test_get_all_candidates():
    api=candidates_api.CandidatesAPI()
    response=api.get_all_candidates()
    assert response.status_code == 200

test_get_all_candidates()

def test_create_new_candidate():
    new_candidate=candidates_api.CandidatesAPI()
    response=new_candidate.create_new_candidate("Jane", "QA")
    json_response = json.loads(response.content)
    assert json_response['candidate']['id'] > 0
    assert json_response['candidate']['name'] == 'Jane'
    assert json_response['candidate']['position'] == 'QA'
    assert response.status_code == 201

test_create_new_candidate()
