
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BE DIVIDE ELSE GREATER ID IF LBRACE LESS LET MINUS MULTIPLY NEWLINE NUMBER PLUS RBRACE SHOUT STRINGprogram : statementsstatements : statements statement\n                  | statementstatement : LET ID BE expression NEWLINEstatement : SHOUT STRING NEWLINEstatement : IF expression LBRACE statements RBRACE\n                 | IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACEexpression : NUMBER\n                  | ID\n                  | expression PLUS expression\n                  | expression LESS expression'
    
_lr_action_items = {'LET':([0,2,3,7,14,15,19,22,23,25,26,27,],[4,4,-3,-2,-5,4,4,-4,-6,4,4,-7,]),'SHOUT':([0,2,3,7,14,15,19,22,23,25,26,27,],[5,5,-3,-2,-5,5,5,-4,-6,5,5,-7,]),'IF':([0,2,3,7,14,15,19,22,23,25,26,27,],[6,6,-3,-2,-5,6,6,-4,-6,6,6,-7,]),'$end':([1,2,3,7,14,22,23,27,],[0,-1,-3,-2,-5,-4,-6,-7,]),'RBRACE':([3,7,14,19,22,23,26,27,],[-3,-2,-5,23,-4,-6,27,-7,]),'ID':([4,6,13,16,17,],[8,12,12,12,12,]),'STRING':([5,],[9,]),'NUMBER':([6,13,16,17,],[11,11,11,11,]),'BE':([8,],[13,]),'NEWLINE':([9,11,12,18,20,21,],[14,-8,-9,22,-10,-11,]),'LBRACE':([10,11,12,20,21,24,],[15,-8,-9,-10,-11,25,]),'PLUS':([10,11,12,18,20,21,],[16,-8,-9,16,16,16,]),'LESS':([10,11,12,18,20,21,],[17,-8,-9,17,17,17,]),'ELSE':([23,],[24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,15,25,],[2,19,26,]),'statement':([0,2,15,19,25,26,],[3,7,3,7,3,7,]),'expression':([6,13,16,17,],[10,18,20,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','my_parser.py',27),
  ('statements -> statements statement','statements',2,'p_statements','my_parser.py',31),
  ('statements -> statement','statements',1,'p_statements','my_parser.py',32),
  ('statement -> LET ID BE expression NEWLINE','statement',5,'p_statement_let','my_parser.py',36),
  ('statement -> SHOUT STRING NEWLINE','statement',3,'p_statement_shout','my_parser.py',40),
  ('statement -> IF expression LBRACE statements RBRACE','statement',5,'p_statement_if','my_parser.py',44),
  ('statement -> IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE','statement',9,'p_statement_if','my_parser.py',45),
  ('expression -> NUMBER','expression',1,'p_expression','my_parser.py',52),
  ('expression -> ID','expression',1,'p_expression','my_parser.py',53),
  ('expression -> expression PLUS expression','expression',3,'p_expression','my_parser.py',54),
  ('expression -> expression LESS expression','expression',3,'p_expression','my_parser.py',55),
]