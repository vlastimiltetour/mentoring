#This is the DAO layer
import json
from dataclasses import asdict
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional
from person import Person, Candidate, Interviewer
from availability import Interview, TimeSlot
#person, interviewer, candidate, TimeSlot


class PersonDao:
    TYPE_MAP = {
        "Person": Person,
        "Candidate": Candidate,
        "Interviewer": Interviewer,
    }

    def __init__(self, storage_file: str = "person.json"):
        self._storage_file = storage_file

    def _load_data(self) -> Dict: #thi is not ideal, opening up every time 
        try:
            with open(self._storage_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            return {}
        
    def _update_data(self, data: Dict):
        with open(self._storage_file, 'w') as f:
            json.dump(data, f, indent=4)

    #create & update
    def save(self, object: Person): #store the pesron type
        data = self._load_data()

        object_dict = asdict(object)
        object_dict["cls_type"] = object.__class__.__name__

        data[str(object.id)] = object_dict
        
        self._update_data(data)
        print(f'saved {object.name} succesfully into database')

    #read
    def get_object_by_id(self, object_id: int) -> Optional[Person]:
        data = self._load_data()
    
        record = data.get(str(object_id))

        if not record:
            return None
        
        cls_name = record.pop("cls_type", "Person")
        cls = self.TYPE_MAP.get(cls_name, Person)

        return cls(**record)
    
    #read
    def list_all(self) -> List[Person]:
        data = self._load_data()
        result = []

        for value in data.values():
            cls_name = value.pop("cls_type", "Person")
            cls = self.TYPE_MAP.get(cls_name, Person)            
            result.append(cls(**value))
        return result
    
    #delete
    def delete(self, object_id) -> bool:
        data = self._load_data()
        object_id = str(object_id)

        if object_id in data:
            del data[object_id]        
            self._update_data(data)
            return True
        
        return False
 
class InterviewDao:
    def __init__(self, storage_file: str = "interviews.json"):
        self._storage_file = storage_file

    def _load_data(self) -> Dict: #thi is not ideal, opening up every time 
        try:
            with open(self._storage_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            return {}
        
    def _update_data(self, data: Dict):
        with open(self._storage_file, 'w') as f:
            json.dump(data, f, indent=4)

    #create & update
    def save(self, object: Interview): #store the pesron type
        data = self._load_data()

        object_dict = asdict(object)
        
        print("object_dict", object_dict)

        data[str(object.id)] = object_dict
        
        self._update_data(data)
        print(f'saved {object.name} succesfully into database')

    #read
    def get_object_by_id(self, object_id: int) -> Optional[Interview]:
        data = self._load_data()
    
        record = data.get(str(object_id))

        if not record:
            return None
        
        cls_name = record.pop("cls_type", "Person")
        cls = self.TYPE_MAP.get(cls_name, Person)

        return cls(**record)
    
    #read
    def list_all(self) -> List[Person]:
        data = self._load_data()
        result = []

        for value in data.values():
            cls_name = value.pop("cls_type", "Person")
            cls = self.TYPE_MAP.get(cls_name, Person)            
            result.append(cls(**value))
        return result
    
    #delete
    def delete(self, object_id) -> bool:
        data = self._load_data()
        object_id = str(object_id)

        if object_id in data:
            del data[object_id]        
            self._update_data(data)
            return True
        
        return False
    

class TimeSlotDao:
    def __init__(self, storage_file: str = "slots.json"):
        self._storage_file = storage_file

    def _load_data(self) -> Dict: #thi is not ideal, opening up every time 
        try:
            with open(self._storage_file, 'r') as f:
                raw_data = json.load(f)
                print(raw_data)
        except (FileNotFoundError,json.JSONDecodeError):
            return {}
        
    def _update_data(self, data: Dict):
        with open(self._storage_file, 'w') as f:
            json.dump(data, f, indent=4)

    #create & update
    def save(self, object: TimeSlot): #store the pesron type
        data = self._load_data()

        object_dict = asdict(object)
        
        print("object_dict", object_dict)

        #convert datetime to isoformat
        
        object_dict["start"] = object.start.isoformat()
        object_dict["end"] = object.end.isoformat()

        #getting ready to update 
        data[str(object.id)] = object_dict
        
        self._update_data(data)
        print(f'saved {object.id, object.} succesfully into database')

    #read
    def get_object_by_id(self, object_id: int) -> Optional[Interview]:
        data = self._load_data()
    
        record = data.get(str(object_id))

        if not record:
            return None
        
        cls_name = record.pop("cls_type", "Person")
        cls = self.TYPE_MAP.get(cls_name, Person)

        return cls(**record)
    
    #read
    def list_all(self) -> List[Person]:
        data = self._load_data()
        result = []

        for value in data.values():
            cls_name = value.pop("cls_type", "Person")
            cls = self.TYPE_MAP.get(cls_name, Person)            
            result.append(cls(**value))
        return result
    
    #delete
    def delete(self, object_id) -> bool:
        data = self._load_data()
        object_id = str(object_id)

        if object_id in data:
            del data[object_id]        
            self._update_data(data)
            return True
        
        return False

