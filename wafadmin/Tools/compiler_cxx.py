#! /usr/bin/env python
# encoding: utf-8

import os,sys,imp,types,ccroot
import optparse
import Utils,Configure,Options
from Logs import debug
cxx_compiler={'win32':['msvc','g++'],'cygwin':['g++'],'darwin':['g++'],'aix5':['g++'],'linux':['g++','icpc','sunc++'],'sunos':['g++','sunc++'],'irix':['g++'],'hpux':['g++'],'default':['g++']}
def __list_possible_compiler(platform):
	try:
		return(cxx_compiler[platform])
	except KeyError:
		return(cxx_compiler["default"])
def detect(conf):
	try:test_for_compiler=Options.options.check_cxx_compiler
	except AttributeError:raise Configure.ConfigurationError("Add set_options(opt): opt.tool_options('compiler_cxx')")
	for compiler in test_for_compiler.split():
		try:
			conf.check_tool(compiler)
		except Configure.ConfigurationError,e:
			debug('compiler_cxx: %r'%e)
		else:
			if conf.env['CXX']:
				conf.check_message(compiler,'',True)
				conf.env['COMPILER_CXX']=compiler
				break
			conf.check_message(compiler,'',False)
def set_options(opt):
	detected_platform=Options.platform
	possible_compiler_list=__list_possible_compiler(detected_platform)
	test_for_compiler=str(" ").join(possible_compiler_list)
	cxx_compiler_opts=opt.add_option_group("C++ Compiler Options")
	cxx_compiler_opts.add_option('--check-cxx-compiler',default="%s"%test_for_compiler,help='On this platform (%s) the following C++ Compiler will be checked by default: "%s"'%(detected_platform,test_for_compiler),dest="check_cxx_compiler")
	for cxx_compiler in test_for_compiler.split():
		opt.tool_options('%s'%cxx_compiler,option_group=cxx_compiler_opts)

