def check_test_type(var, tests):
	assert type(var) == str, 'not a string'
	assert var in tests.keys(), 'unknown test type'
	return var



class Testing():
	def __init__(self, model, test_type, follow_up_testing_interval,
		screening_interval_patients, screening_interval_employees,
		liberating_testing, K1_areas, verbosity):

		self.follow_up_testing_interval = follow_up_testing_interval
		self.screening_interval_patients = screening_interval_patients
		self.screening_interval_employees = screening_interval_employees
		self.liberating_testing = liberating_testing
		self.model = model
		self.verbosity = verbosity
		self.K1_areas = K1_areas

		self.tests = {
		'same_day_antigen':
	     {
	         'sensitivity':0.9756,
	         'specificity':0.999,
	         'time_until_testable':2,
	         'time_testable':6,
	         'time_until_test_result':0
	     },
		'one_day_antigen':
	     {
	         'sensitivity':0.9756,
	         'specificity':0.999,
	         'time_until_testable':2,
	         'time_testable':6,
	         'time_until_test_result':1
	     },
		'two_day_antigen':
	     {
	         'sensitivity':0.9756,
	         'specificity':0.999,
	         'time_until_testable':2,
	         'time_testable':6,
	         'time_until_test_result':2
	     },
	     'same_day_PCR':
	     {
	         'sensitivity':0.9652,
	         'specificity':1,
	         'time_until_testable':0,
	         'time_testable':model.infection_duration,
	         'time_until_test_result':0
	     },
	     'one_day_PCR':
	     {
	         'sensitivity':0.9652,
	         'specificity':1,
	         'time_until_testable':0,
	         'time_testable':model.infection_duration,
	         'time_until_test_result':1
	     },
	      'two_day_PCR':
	     {
	         'sensitivity':0.9652,
	         'specificity':1,
	         'time_until_testable':0,
	         'time_testable':model.infection_duration,
	         'time_until_test_result':2
	     },
	    'same_day_LAMP':
	     {
	         'sensitivity':0.9652,
	         'specificity':0.9968,
	         'time_until_testable':0,
	         'time_testable':model.infection_duration,
	         'time_until_test_result':0
	     },
	    'one_day_LAMP':
	     {
	         'sensitivity':0.9652,
	         'specificity':0.9968,
	         'time_until_testable':0,
	         'time_testable':model.infection_duration,
	         'time_until_test_result':1
	     },
	    'two_day_LAMP':
	     {
	         'sensitivity':0.9652,
	         'specificity':0.9968,
	         'time_until_testable':0,
	         'time_testable':model.infection_duration,
	         'time_until_test_result':2
	     }
	    }

		self.test_type = check_test_type(test_type, self.tests)
		self.sensitivity = self.tests[self.test_type]['sensitivity']
		self.specificity = self.tests[self.test_type]['specificity']
		self.time_until_testable = self.tests[self.test_type]['time_until_testable']
		self.time_testable = self.tests[self.test_type]['time_testable']
		self.time_until_test_result = self.tests[self.test_type]['time_until_test_result']




