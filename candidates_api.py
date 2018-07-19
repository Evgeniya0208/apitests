import requests
class CandidatesAPI:
    def get_all_candidates(self):
        return requests.get("http://qainterview.cogniance.com/candidates")


    def create_new_candidate(self, name, position):

        resp = requests.post("http://qainterview.cogniance.com/candidates", json = {'name':name, 'position':position})
        return  resp
