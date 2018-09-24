import unittest
import random
import a2

NUCLEOTIDE = ['A', 'T', 'G', 'C']


def build_id(tag):
    return str(tag) + str(random.randint(10000, 50000))


def build_marker():
    return 'mk' + str(random.randint(10000, 50000))


def build_chromosome():
    return ''.join(random.choices(NUCLEOTIDE, k=2))


class _TestGenericHumanClass(unittest.TestCase):
    ''' Test generic human class '''

    def _test_set_get_by_pos_one_pair(self, human):
        chromosome = build_chromosome()
        human.set_by_pos(6, 42, chromosome)
        self.assertEqual(chromosome, human.get_by_pos(6, 42),
                         'Failed to set chromosome "%s" for pair %d at position %d.' % (chromosome, 6, 42))

    def _test_set_get_by_pos_multiple_pairs(self, human):
        chromosome1 = build_chromosome()
        chromosome2 = build_chromosome()
        chromosome3 = build_chromosome()
        human.set_by_pos(6, 42, chromosome1)
        human.set_by_pos(6, 43, chromosome2)
        human.set_by_pos(18, 42, chromosome3)
        self.assertEqual(chromosome1, human.get_by_pos(6, 42),
                         'Failed to set chromosome "%s" for pair %d at position %d.' % (chromosome1, 6, 42))
        self.assertEqual(chromosome2, human.get_by_pos(6, 43),
                         'Failed to set chromosome "%s" for pair %d at position %d.' % (chromosome2, 6, 43))
        self.assertEqual(chromosome3, human.get_by_pos(18, 42),
                         'Failed to set chromosome "%s" for pair %d at position %d.' % (chromosome3, 18, 42))

    def _test_set_get_by_marker_one_marker(self, human):
        marker = build_marker()
        chromosome = build_chromosome()
        human.set_marker(marker, 7, 42)
        human.set_by_marker(marker, chromosome)
        self.assertEqual(chromosome, human.get_by_marker(marker),
                         'Failed to set chromosome "%s" to marker "%s" for pair %d at position %d.'
                         % (chromosome, marker, 7, 42))

    def _test_set_get_by_marker_multiple_markers(self, human):
        marker1 = build_marker()
        chromosome1 = build_chromosome()
        marker2 = build_marker()
        chromosome2 = build_chromosome()
        marker3 = build_marker()
        chromosome3 = build_chromosome()
        human.set_marker(marker1, 7, 42)
        human.set_by_marker(marker1, chromosome1)
        human.set_marker(marker2, 7, 18)
        human.set_by_marker(marker2, chromosome2)
        human.set_marker(marker3, 22, 42)
        human.set_by_marker(marker3, chromosome3)
        self.assertEqual(chromosome1, human.get_by_marker(marker1),
                         'Failed to set chromosome "%s" to marker "%s" for pair %d at position %d.'
                         % (chromosome1, marker1, 7, 42))
        self.assertEqual(chromosome2, human.get_by_marker(marker2),
                         'Failed to set chromosome "%s" to marker "%s" for pair %d at position %d.'
                         % (chromosome2, marker2, 7, 42))
        self.assertEqual(chromosome3, human.get_by_marker(marker3),
                         'Failed to set chromosome "%s" to marker "%s" for pair %d at position %d.'
                         % (chromosome3, marker3, 7, 42))

    def _test_get_chromosome_from_chromosome_pair(self, human):
        chromosome = build_chromosome()
        ch = human.get_chromosome(18)
        ch.set_by_pos(42, chromosome)
        self.assertEqual(chromosome, human.get_by_pos(18, 42),
                         'Failed to get chromosome from pair %d then set "%s" at position %d.' % (18, chromosome, 42))

    def _test_get_chromosome_from_marker_pair(self, human):
        marker = build_marker()
        chromosome1 = build_chromosome()
        human.set_marker(marker, 15, 77)
        human.set_by_marker(marker, chromosome1)
        chromosome2 = build_chromosome()
        ch = human.get_chromosome(15)
        ch.set_by_pos(42, chromosome2)
        self.assertEqual(chromosome1, human.get_by_marker(marker),
                         'Failed to set chromosome "%s" to marker "%s" for pair %d at position %d.'
                         % (chromosome1, marker, 7, 42))
        self.assertEqual(chromosome2, human.get_by_pos(15, 42),
                         'Failed to get chromosome from marker pair %d, then set "%s" at position %d.'
                         % (15, chromosome2, 42))

    def _test_set_get_chromosome(self, human):
        chromosome = build_chromosome()
        ch = human.get_chromosome(11)
        ch.set_by_pos(22, chromosome)
        self.assertEqual(chromosome, human.get_by_pos(11, 22),
                         'Failed to get chromosome from pair %d, then set "%s" at position %d.' % (11, chromosome, 22))
        human.set_chromosome(8, ch)
        self.assertEqual(chromosome, human.get_by_pos(8, 22),
                         'Failed to get chromosome from pair (%d-%d), then set "%s" for new chromosome pair (%d-%d).'
                         % (11, 22, chromosome, 8, 22))

    def _test_set_get_by_pos_lower_boundary_index(self, human):
        chromosome = build_chromosome()
        human.set_by_pos(0, 42, chromosome)
        self.assertEqual(chromosome, human.get_by_pos(0, 42),
                         'Failed to set chromosome "%s" for pair %d at position %d. It\'s 0-indexing!' % (chromosome, 0, 42))

    def _test_set_get_by_pos_upper_boundary_index(self, human):
        chromosome = build_chromosome()
        human.set_by_pos(22, 84, chromosome)
        self.assertEqual(chromosome, human.get_by_pos(22, 84),
                         'Failed to set chromosome "%s" for pair %d at position %d. It\'s 0-indexing!' % (chromosome, 22, 84))

        # def _test_invalid_pair_and_position(self, human):
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (11, -10)):
        #         human.set_by_pos(-1, 42, build_chromosome())
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d). It\'s 0-indexing!' % (11, -10)):
        #         human.set_by_pos(23, 42, build_chromosome())
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (11, -10)):
        #         human.set_by_pos(-1, -1, build_chromosome())
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (11, -10)):
        #         human.set_by_pos(23, -1, build_chromosome())


class TestA2_Male(_TestGenericHumanClass):
    ''' Test A2 Male class '''

    def setUp(self):
        self.male = a2.Male(build_id('male'))

    def test_init(self):
        self.assertIsNotNone(a2.Male(build_id('m')), 'Failed to create Male object.')

    def test_inheritance(self):
        self.assertFalse(issubclass(a2.Male, a2.Female), 'Male should be a subclass of Female.')

    def test_set_get_by_pos_one_pair(self):
        self._test_set_get_by_pos_one_pair(self.male)

    def test_set_get_by_pos_one_pair_and_replace_same_pair(self):
        chromosome1 = build_chromosome()
        self.male.set_by_pos(6, 42, chromosome1)
        self.assertEqual(chromosome1, self.male.get_by_pos(6, 42),
                         'Failed to set chromosome "%s" for pair %d at position %d.' % (chromosome1, 6, 42))
        chromosome2 = build_chromosome()
        self.male.set_by_pos(6, 42, chromosome2)
        self.assertEqual(chromosome2, self.male.get_by_pos(6, 42),
                         'Failed to set chromosome "%s" for pair %d at position %d.' % (chromosome2, 6, 42))

    def test_set_get_by_pos_multiple_pairs(self):
        self._test_set_get_by_pos_multiple_pairs(self.male)

    def test_set_get_by_marker_one_marker(self):
        self._test_set_get_by_marker_one_marker(self.male)

    def test_set_get_by_marker_multiple_markers(self):
        self._test_set_get_by_marker_multiple_markers(self.male)

    def test_get_chromosome_from_chromosome_pair(self):
        self._test_get_chromosome_from_chromosome_pair(self.male)

    def test_get_chromosome_from_marker_pair(self):
        self._test_get_chromosome_from_marker_pair(self.male)

    def test_set_get_chromosome(self):
        self._test_set_get_chromosome(self.male)

    # def test_invalid_pair_and_position(self):
    #     self._test_invalid_pair_and_position(self.male)

    def test_set_get_by_pos_lower_boundary_index(self):
        self._test_set_get_by_pos_lower_boundary_index(self.male)

    def test_set_get_by_pos_upper_boundary_index(self):
        self._test_set_get_by_pos_upper_boundary_index(self.male)


class TestA2_Female(_TestGenericHumanClass):
    ''' Test A2 Female class '''

    def setUp(self):
        self.female = a2.Female(build_id('female'))

    def test_init(self):
        self.assertIsNotNone(a2.Female(build_id('f')), 'Failed to create Female object.')

    def test_inheritance(self):
        self.assertFalse(issubclass(a2.Female, a2.Male), 'Female should not be a subclass of Male.')

    def test_set_get_by_pos_one_pair(self):
        self._test_set_get_by_pos_one_pair(self.female)

    def test_set_get_by_pos_multiple_pairs(self):
        self._test_set_get_by_pos_multiple_pairs(self.female)

    def test_set_get_by_marker_one_marker(self):
        self._test_set_get_by_marker_one_marker(self.female)

    def test_set_get_by_marker_multiple_markers(self):
        self._test_set_get_by_marker_multiple_markers(self.female)

    def test_get_chromosome_from_chromosome_pair(self):
        self._test_get_chromosome_from_chromosome_pair(self.female)

    def test_get_chromosome_from_marker_pair(self):
        self._test_get_chromosome_from_marker_pair(self.female)

    def test_set_get_chromosome(self):
        self._test_set_get_chromosome(self.female)

    # def test_invalid_pair_and_position(self):
    #     self._test_invalid_pair_and_position(self.female)

    def test_set_get_by_pos_lower_boundary_index(self):
        self._test_set_get_by_pos_lower_boundary_index(self.female)

    def test_set_get_by_pos_upper_boundary_index(self):
        self._test_set_get_by_pos_upper_boundary_index(self.female)

    def test_procreate_no_child_chromosome_set(self):
        father = a2.Male(build_id('m'))
        mother = a2.Female(build_id('f'))
        binder = a2.Binder()
        binder.set_sex('F')
        child = mother.procreate(father, binder)
        self.assertIsNotNone(child, 'Failed to procreate child (Female). No Female object is created.')
        self.assertFalse(isinstance(child, a2.Male), 'Type check failed, procreated child should be a Male object.')
        self.assertTrue(isinstance(child, a2.Female), 'Type check failed, procreated child should not be a Female object.')

    def test_procreate_child_child_chromosome_set(self):
        chromosome_m1, chromosome_f1 = 'AC', 'GA'
        chromosome_m2, chromosome_f2 = 'CT', 'TG'
        # set up father chromosome
        father = a2.Male(build_id('m'))
        father.set_by_pos(17, 42, chromosome_m1)
        father.set_by_pos(10, 84, chromosome_m2)
        self.assertEqual(chromosome_m1, father.get_by_pos(17, 42),
                         'Failed to set father chromosome "%s" to %d-%d.' % (chromosome_m1, 17, 42))
        self.assertEqual(chromosome_m2, father.get_by_pos(10, 84),
                         'Failed to set father chromosome "%s" to %d-%d.' % (chromosome_m2, 10, 84))
        # set up mother chromosome
        mother = a2.Female(build_id('f'))
        mother.set_by_pos(17, 42, chromosome_f1)
        mother.set_by_pos(10, 84, chromosome_f2)
        self.assertEqual(chromosome_f1, mother.get_by_pos(17, 42),
                         'Failed to set mother chromosome "%s" to %d-%d.' % (chromosome_f1, 17, 42))
        self.assertEqual(chromosome_f2, mother.get_by_pos(10, 84),
                         'Failed to set mother chromosome "%s" to %d-%d.' % (chromosome_f2, 10, 84))
        # set up binder chromosome
        binder = a2.Binder()
        binder.set_sex('F')
        binder.set_by_pos(17, 42, 'RM')
        binder.set_by_pos(10, 84, 'LM')
        # procreate child
        child = mother.procreate(father, binder)
        self.assertIsNotNone(child, 'Failed to procreate child. No Female object is created.')
        self.assertTrue(isinstance(child, a2.Female), 'Type check failed, procreated child should be a Female object.')
        self.assertEqual('AA', child.get_by_pos(17, 42), 'Child chromosome at %d-%d is incorrect.' % (17, 42))
        self.assertEqual('TT', child.get_by_pos(10, 84), 'Child chromosome at %d-%d is incorrect.' % (10, 84))


class TestA2_Query(unittest.TestCase):
    ''' Test A2 Query class '''

    def test_init(self):
        self.assertIsNotNone(a2.Query(), 'Failed to create Query object.')

    def test_inheritance(self):
        self.assertFalse(issubclass(a2.Query, a2.Male), 'Query should not be a subclass of Male.')
        self.assertFalse(issubclass(a2.Query, a2.Female), 'Query should not be a subclass of Female.')
        self.assertFalse(issubclass(a2.Query, a2.Binder), 'Query should not be a subclass of Binder.')

    def test_query_set_by_pos(self):
        chromosome = build_chromosome()
        # set up father
        father = a2.Male(build_id('m'))
        father.set_by_pos(17, 42, chromosome)
        # set up query
        query = a2.Query()
        query.set_by_pos(17, 42, chromosome)
        self.assertTrue(father.test(query),
                        'Failed to test the query. Chromosome "%s" is set to (%d-%d)' % (chromosome, 17, 42))

    def test_query_set_by_marker(self):
        chromosome = random.choice(NUCLEOTIDE) + 'G'
        marker = build_marker()
        # setup mother
        mother = a2.Female(build_id('f'))
        mother.set_by_pos(9, 76, chromosome)
        # set up query
        query = a2.Query()
        query.set_marker(marker, 9, 76)
        query.set_by_marker(marker, '3G')
        self.assertTrue(mother.test(query),
                        'Failed to test the query. Chromosome "%s" is set to (%d-%d)' % (chromosome, 9, 76))

    def test_query_diff_chromosome_same_pair_position(self):
        chromosome1, chromosome2 = 'AG', 'CT'
        # set up father
        mother = a2.Female(build_id('f'))
        mother.set_by_pos(17, 42, chromosome1)
        # set up query
        query = a2.Query()
        query.set_by_pos(17, 42, chromosome2)
        self.assertFalse(mother.test(query),
                         'Failed to test the query. Both chromosome is set to (%d-%d), but Mother chromosome is "%s", Query chromosome is "%s".'
                         % (17, 42, chromosome1, chromosome2))

    def test_query_same_chromosome_diff_sex_chromosome_pair(self):
        chromosome = build_chromosome()
        # set up father
        father = a2.Male(build_id('m'))
        father.set_by_pos(11, 42, chromosome)
        # set up query
        query = a2.Query()
        query.set_by_pos(22, 42, chromosome)
        self.assertFalse(father.test(query),
                         'Failed to test the query. Chromosome is "%s". Father chromosome is set to (%d-%d), but query chromosome is set to (%d-%d)'
                         % (chromosome, 11, 42, 22, 42))

        # def test_set_invalid_pair_and_position(self):
        #     query = a2.Query()
        #     chromosome = build_chromosome()
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (-10, 42)):
        #         query.set_by_pos(-10, 42, chromosome)
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d). It\'s 0-indexing!' % (23, 42)):
        #         query.set_by_pos(23, 42, chromosome)
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (11, -10)):
        #         query.set_by_pos(11, -10, chromosome)


class TestA2_Binder(unittest.TestCase):
    ''' Test A2 Binder class '''

    def setUp(self):
        self.binder = a2.Binder()

    def test_init(self):
        self.assertIsNotNone(a2.Binder(), 'Failed to create Binder object.')

    def test_inheritance(self):
        self.assertFalse(issubclass(a2.Binder, a2.Male), 'Binder should not be a subclass of Male.')
        self.assertFalse(issubclass(a2.Binder, a2.Female), 'Binder should not be a subclass of Female.')
        self.assertFalse(issubclass(a2.Binder, a2.Query), 'Binder should not be a subclass of Query.')

    def test_set_by_pos_boundary_index_and_check_child_index(self):
        chromosome_m1, chromosome_f1 = 'CT', 'AC'
        chromosome_m2, chromosome_f2 = 'AG', 'GT'
        # set up father chromosome
        father = a2.Male(build_id('m'))
        father.set_by_pos(0, 42, chromosome_m1)
        father.set_by_pos(22, 84, chromosome_m2)
        # self.assertEqual(chromosome_m1, father.get_by_pos(0, 42),
        #                  'Failed to set father chromosome "%s" to %d-%d.' % (chromosome_m1, 0, 42))
        # self.assertEqual(chromosome_m2, father.get_by_pos(22, 84),
        #                  'Failed to set father chromosome "%s" to %d-%d.' % (chromosome_m2, 22, 84))
        # set up mother chromosome
        mother = a2.Female(build_id('f'))
        mother.set_by_pos(0, 42, chromosome_f1)
        mother.set_by_pos(22, 84, chromosome_f2)
        # self.assertEqual(chromosome_f1, mother.get_by_pos(0, 42),
        #                  'Failed to set mother chromosome "%s" to %d-%d.' % (chromosome_f1, 0, 42))
        # self.assertEqual(chromosome_f2, mother.get_by_pos(22, 84),
        #                  'Failed to set mother chromosome "%s" to %d-%d.' % (chromosome_f2, 22, 84))
        # set up binder chromosome
        binder = a2.Binder()
        binder.set_sex('M')
        binder.set_by_pos(0, 42, 'RM')
        binder.set_by_pos(22, 84, 'LM')
        # procreate child
        child = mother.procreate(father, binder)
        # self.assertIsNotNone(child, 'Failed to procreate child (Male). No Male object is created.')
        # self.assertTrue(isinstance(child, a2.Male), 'Type check failed, procreated child should be a Male object.')
        self.assertEqual('CC', child.get_by_pos(0, 42), 'Child chromosome at %d-%d is incorrect.' % (0, 42))
        self.assertEqual('GG', child.get_by_pos(22, 84), 'Child chromosome at %d-%d is incorrect.' % (22, 84))

        # def test_set_invalid_pair_and_position(self):
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (-10, 42)):
        #         self.binder.set_by_pos(-10, 42, 'LM')
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d). It\'s 0-indexing!' % (23, 42)):
        #         self.binder.set_by_pos(23, 42, 'RM')
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (11, -10)):
        #         self.binder.set_by_pos(11, -10, 'LM')
        #     with self.assertRaises(Exception, msg='Failed to raise exception when set pair (%d-%d)' % (-1, -10)):
        #         self.binder.set_by_pos(-1, -10, 'LM')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
