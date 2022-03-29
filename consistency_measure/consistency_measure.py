class ConsistencyMeasure:
    def __init__(self, supremum, infimum):
        if len(supremum) != len(infimum):
            raise Exception('Different sizes of distributions!')
        self.infimum = infimum
        self.supremum = supremum
        self.distributions_len = len(self.infimum)
        if self.distributions_len == 0:
            raise Exception('Empty distributions arrays!')
        self.__get_order()
        self.__get_comparison_signs()
        self.__get_distance_between_supremum_and_infimum()

    def __get_order(self):
        self.indexes_in_order = [i[0] for i in sorted(enumerate(self.infimum), key=lambda x:x[1], reverse=True)]

    
    def __get_comparison_signs(self):
        self.ordered_supremum = [self.supremum[i] for i in self.indexes_in_order]
        self.ordered_infimum = [self.infimum[i] for i in self.indexes_in_order]
        self.supremum_comparison_signs = []
        self.infimum_comparison_signs = []

        for i in range(self.distributions_len):
            if i < self.distributions_len - 1:
                if self.ordered_supremum[i] > self.ordered_supremum[i+1]:
                    self.supremum_comparison_signs.append(1)
                else:
                    self.supremum_comparison_signs.append(0)
            else:
                if self.ordered_supremum[i] > 0:
                    self.supremum_comparison_signs.append(1)
                else:
                    self.supremum_comparison_signs.append(0)

        for i in range(self.distributions_len):
            if i < self.distributions_len - 1:
                if self.ordered_infimum[i] > self.ordered_infimum[i+1]:
                    self.infimum_comparison_signs.append(1)
                else:
                    self.infimum_comparison_signs.append(0)
            else:
                if self.ordered_infimum[i] > 0:
                    self.infimum_comparison_signs.append(1)
                else:
                    self.infimum_comparison_signs.append(0)

        print('supremum comparison signs - {}'.format(self.supremum_comparison_signs))
        print('infimum comparison signs - {}'.format(self.infimum_comparison_signs))

    def get_max_possible_distance(self):
        self.max_length = self.distributions_len * 2 - 1
        print('max distance - {}'.format(self.max_length))
        return self.max_length

    def __get_distance_between_supremum_and_infimum(self):
        sup = self.supremum_comparison_signs.copy()
        self.counter = 0
        self.graph_traversal(sup, 0)
        print('distance between supremum and infimum - {}'.format(self.counter))
        return self.counter


    def graph_traversal(self, sup, counter):
        # print('sup - {}'.format(sup))
        if sup == self.infimum_comparison_signs:
            self.counter = counter
            return 0
        if sup == [0] * self.distributions_len:
            return 0
        end = self.distributions_len
        while end > 0 and sup[end-1] == 0:
            end -= 1
        for i in range(end):
            if sup[i] == 0:
                new_sup = sup.copy()
                new_sup[i] = 1
                self.graph_traversal(new_sup, counter+1)
                # print('new sup 1 - {}'.format(new_sup))
        if end - 1 > 0 and sup[end-1] == 1 and sup[end-2] == 1:
            new_sup = sup.copy()
            new_sup[end-1] = 0
            self.graph_traversal(new_sup, counter+1)
            # print('new sup 2 - {}'.format(new_sup))

        if end == 1 and sup[0] == 1:
            new_sup = sup.copy()
            new_sup[end-1] = 0
            self.graph_traversal(new_sup, counter+1)

    
    def get_counter(self):
        return self.counter


    def __str__(self):
        return '''
        supremum - {},
        infimum - {},
        reordered indexes - {}
               '''.format(self.supremum, self.infimum, self.indexes_in_order)
        