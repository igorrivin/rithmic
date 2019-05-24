# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ticker_plant_proto_pool.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import request_login_pb2 as request__login__pb2
import response_login_pb2 as response__login__pb2
import request_logout_pb2 as request__logout__pb2
import response_logout_pb2 as response__logout__pb2
import request_reference_data_pb2 as request__reference__data__pb2
import response_reference_data_pb2 as response__reference__data__pb2
import reject_pb2 as reject__pb2
import request_market_data_update_pb2 as request__market__data__update__pb2
import response_market_data_update_pb2 as response__market__data__update__pb2
import request_give_tick_size_type_table_pb2 as request__give__tick__size__type__table__pb2
import response_give_tick_size_type_table_pb2 as response__give__tick__size__type__table__pb2
import request_get_instrument_by_underlying_pb2 as request__get__instrument__by__underlying__pb2
import response_get_instrument_by_underlying_pb2 as response__get__instrument__by__underlying__pb2
import response_get_instrument_by_underlying_keys_pb2 as response__get__instrument__by__underlying__keys__pb2
import request_market_data_update_by_underlying_pb2 as request__market__data__update__by__underlying__pb2
import response_market_data_update_by_underlying_pb2 as response__market__data__update__by__underlying__pb2
import best_bid_offer_pb2 as best__bid__offer__pb2
import order_book_pb2 as order__book__pb2
import last_trade_pb2 as last__trade__pb2
import trade_statistics_pb2 as trade__statistics__pb2
import quote_statistics_pb2 as quote__statistics__pb2
import indicator_prices_pb2 as indicator__prices__pb2
import open_interest_pb2 as open__interest__pb2
import end_of_day_prices_pb2 as end__of__day__prices__pb2
import market_mode_pb2 as market__mode__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ticker_plant_proto_pool.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1dticker_plant_proto_pool.proto\x1a\x13request_login.proto\x1a\x14response_login.proto\x1a\x14request_logout.proto\x1a\x15response_logout.proto\x1a\x1crequest_reference_data.proto\x1a\x1dresponse_reference_data.proto\x1a\x0creject.proto\x1a request_market_data_update.proto\x1a!response_market_data_update.proto\x1a\'request_give_tick_size_type_table.proto\x1a(response_give_tick_size_type_table.proto\x1a*request_get_instrument_by_underlying.proto\x1a+response_get_instrument_by_underlying.proto\x1a\x30response_get_instrument_by_underlying_keys.proto\x1a.request_market_data_update_by_underlying.proto\x1a/response_market_data_update_by_underlying.proto\x1a\x14\x62\x65st_bid_offer.proto\x1a\x10order_book.proto\x1a\x10last_trade.proto\x1a\x16trade_statistics.proto\x1a\x16quote_statistics.proto\x1a\x16indicator_prices.proto\x1a\x13open_interest.proto\x1a\x17\x65nd_of_day_prices.proto\x1a\x11market_mode.proto')
  ,
  dependencies=[request__login__pb2.DESCRIPTOR,response__login__pb2.DESCRIPTOR,request__logout__pb2.DESCRIPTOR,response__logout__pb2.DESCRIPTOR,request__reference__data__pb2.DESCRIPTOR,response__reference__data__pb2.DESCRIPTOR,reject__pb2.DESCRIPTOR,request__market__data__update__pb2.DESCRIPTOR,response__market__data__update__pb2.DESCRIPTOR,request__give__tick__size__type__table__pb2.DESCRIPTOR,response__give__tick__size__type__table__pb2.DESCRIPTOR,request__get__instrument__by__underlying__pb2.DESCRIPTOR,response__get__instrument__by__underlying__pb2.DESCRIPTOR,response__get__instrument__by__underlying__keys__pb2.DESCRIPTOR,request__market__data__update__by__underlying__pb2.DESCRIPTOR,response__market__data__update__by__underlying__pb2.DESCRIPTOR,best__bid__offer__pb2.DESCRIPTOR,order__book__pb2.DESCRIPTOR,last__trade__pb2.DESCRIPTOR,trade__statistics__pb2.DESCRIPTOR,quote__statistics__pb2.DESCRIPTOR,indicator__prices__pb2.DESCRIPTOR,open__interest__pb2.DESCRIPTOR,end__of__day__prices__pb2.DESCRIPTOR,market__mode__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
