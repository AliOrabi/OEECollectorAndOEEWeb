#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from random import randint

class DbTools(object):
    def __init__(self):
        self.dboee = DAL('sqlite://oee.db', pool_size=0, migrate=False)
        self.session = current.session
        self.request = current.request
        self.response = current.response
        self.cache = current.cache
        self.define_table()

    def define_table(self):
        self.tblOee_Country = self.dboee.define_table('tblOee_Country', \
                       Field('fldOeeCountryTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryNr', 'integer', label='Country nr', readable=False, writable=False), \
                       Field('fldOeeCountryDescription', 'string', label='Country description'), \
                       Field('fldOeeCountryInformation', 'string', label='Country information'), \
                       Field('fldOeeCountryLanguageID', 'integer', label='Language ID', readable=False, writable=False), \
                       Field('fldOeeCountryHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Plant = self.dboee.define_table('tblOee_Plant', \
                       Field('fldOeePlantTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country', readable=False, writable=False), \
                       Field('fldOeePlantNr', 'integer', label='Plant nr', readable=False, writable=False), \
                       Field('fldOeePlantDescription', 'string', label='Plant description'), \
                       Field('fldOeePlantInformation', 'string', label='Plant information'), \
                       Field('fldOeePlantHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_SubPlant = self.dboee.define_table('tblOee_SubPlant', \
                       Field('fldOeeSubPlantTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country', readable=False, writable=False), \
                       Field('fldOeePlantID', 'integer', label='Plant', readable=False, writable=False), \
                       Field('fldOeeSubPlantNr', 'integer', label='Sub-Plant nr', readable=False, writable=False), \
                       Field('fldOeeSubPlantDescription', 'string', label='Sub-Plant description'), \
                       Field('fldOeeSubPlantInformation', 'string', label='Sub-Plant information'), \
                       Field('fldOeeSubPlantHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Department = self.dboee.define_table('tblOee_Department', \
                       Field('fldOeeDepartmentTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country', readable=False, writable=False), \
                       Field('fldOeePlantID', 'integer', label='Plant', readable=False, writable=False), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant', readable=False, writable=False), \
                       Field('fldOeeDepartmentNr', 'integer', label='Department nr', readable=False, writable=False), \
                       Field('fldOeeDepartmentDescription', 'string', label='Department department'), \
                       Field('fldOeeDepartmentInformation', 'string', label='Department information'), \
                       Field('fldOeeDepartmentHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_ActivityGroup = self.dboee.define_table('tblOee_ActivityGroup', \
                       Field('fldOeeActivityGroupTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeActivityGroupNr', 'integer', label='Activitygroup'), \
                       Field('fldOeeActivityGroupDescription', 'text', label='Activitygroup description'), \
                       Field('fldOeeActivityGroupInformation', 'text', label='Activitygroup information'), \
                       Field('fldOeeActivityGroupColorNr', 'integer', label='Activitygroup color'), \
                       Field('fldOeeActivityGroupCalcForOee', 'integer', label='Calculate OEE'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Activity = self.dboee.define_table('tblOee_Activity', \
                       Field('fldOeeActivityTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeActivityNr', 'integer', label='Activity nr'), \
                       Field('fldOeeActivityGroupID', 'integer', label='Activitygroup'), \
                       Field('fldOeeActivityDescription', 'string', label='Activity description'), \
                       Field('fldOeeActivityInformation', 'string', label='Activity information'), \
                       Field('fldOeeActivityHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_ModuleSensorStyle = self.dboee.define_table('tblOee_ModuleSensorStyle', \
                       Field('fldOeeModuleSensorStyleTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeeModuleSensorStyleNr', 'integer', label='Sensor-style nr'), \
                       Field('fldOeeModuleSensorStyleDescription', 'string', label='Sensor-style'), \
                       Field('fldOeeModuleSensorStyleInformation', 'string', label='Sensor-style information'), \
                       Field('fldOeeModuleSensorStyleHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_ModuleType = self.dboee.define_table('tblOee_ModuleType', \
                       Field('fldOeeModuleTypeTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeModuleTypeNr', 'integer', label='Module-type nr'), \
                       Field('fldOeeModuleTypeConnection', 'string', label='Connection-type'), \
                       Field('fldOeeModuleTypeDescription', 'string', label='Module-type description'), \
                       Field('fldOeeModuleTypeInformation', 'string', label='Connection-type information'), \
                       Field('fldOeeModuleTypeHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Module = self.dboee.define_table('tblOee_Module', \
                       Field('fldOeeModuleTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeModuleNr', 'integer', label='Module nr'), \
                       Field('fldOeeModuleTypeID', 'integer', label='Module-type'), \
                       Field('fldOeeModuleSensorStyleID', 'integer', label='Sensor-style'), \
                       Field('fldOeeModuleDescription', 'string', label='Module description'), \
                       Field('fldOeeModuleInformation', 'string', label='Module information'), \
                       Field('fldOeeModuleIpAddress', 'string', label='IP address'), \
                       Field('fldOeeModuleIpAddressPort', 'integer', label='IP Port'), \
                       Field('fldOeeModuleComPort', 'string', label='Com port'), \
                       Field('fldOeeModuleBitsPerSecond', 'integer', label='Bits per Second'), \
                       Field('fldOeeModuleDatabits', 'integer', label='Databits'), \
                       Field('fldOeeModuleStopBits', 'integer', label='StopBits'), \
                       Field('fldOeeModuleFlowControl', 'string', label='Flowcontrol'), \
                       Field('fldOeeModuleSensorAddress', 'integer', label='Sensor address'), \
                       Field('fldOeeModuleSensorResetAddress', 'integer', label='Sensor reset address'), \
                       Field('fldOeeModuleParity', 'string', label='Parity'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeModuleHistory', 'boolean', label='History'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineIOFailure = self.dboee.define_table('tblOee_MachineIOFailure', \
                       Field('fldOeeMachineIOFailureTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineIOFailureNr', 'integer', label='I/O failure nr'), \
                       Field('fldOeeMachineIOFailureDescription', 'string', label='I/O failure'), \
                       Field('fldOeeMachineIOFailureInformation', 'string', label='I/O failure information'), \
                       Field('fldOeeMachineIOFailureHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineShortbreak = self.dboee.define_table('tblOee_MachineShortbreak', \
                       Field('fldOeeMachineShortBreakTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineShortBreakNr', 'integer', label='Shortbreak nr'), \
                       Field('fldOeeMachineShortBreakDescription', 'string', label='Shortbreak description'), \
                       Field('fldOeeMachineShortBreakInformation', 'string', label='Shortbreak information'), \
                       Field('fldOeeMachineShortBreakHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineStatus = self.dboee.define_table('tblOee_MachineStatus', \
                       Field('fldOeeMachineStatusTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineStatusNr', 'integer', label='Machine status nr'), \
                       Field('fldOeeMachineStatusDescription', 'string', label='Machine status description'), \
                       Field('fldOeeMachineStatusInformation', 'string', label='Machine status information'), \
                       Field('fldOeeMachineStatusHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineUndefinedProduction = self.dboee.define_table('tblOee_MachineUndefinedProduction', \
                       Field('fldOeeMachineUndefinedProductionTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUndefinedProductionNr', 'integer', label='Undefined Production nr'), \
                       Field('fldOeeMachineUndefinedProductionDescription', 'string', label='Undefined Production description'), \
                       Field('fldOeeMachineUndefinedProductionInformation', 'string', label='Undefined Production information'), \
                       Field('fldOeeMachineUndefinedProductionHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineUndefinedStandstill = self.dboee.define_table('tblOee_MachineUndefinedStandstill', \
                       Field('fldOeeMachineUndefinedStandstillTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUndefinedStandstillNr', 'integer', label='Undefined standstill nr'), \
                       Field('fldOeeMachineUndefinedStandstillDescription', 'string', label='Undefined standstill description'), \
                       Field('fldOeeMachineUndefinedStandstillInformation', 'string', label='Undefined standstill information'), \
                       Field('fldOeeMachineUndefinedStandstillHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineUnscheduled = self.dboee.define_table('tblOee_MachineUnscheduled', \
                       Field('fldOeeMachineUnscheduledTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUnscheduledNr', 'integer', label='Unscheduled nr'), \
                       Field('fldOeeMachineUnscheduledDescription', 'string', label='Unscheduled description'), \
                       Field('fldOeeMachineUnscheduledInformation', 'string', label='Unscheduled information'), \
                       Field('fldDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeMachineUnscheduledHistory', 'boolean', label='History'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineUnit = self.dboee.define_table('tblOee_MachineUnit', \
                       Field('fldOeeMachineUnitTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUnitNr', 'integer', label='Machine-unit nr'), \
                       Field('fldOeeMachineUnitDescription', 'string', label='Machine-unit description'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeMachineUnitHistory', 'boolean', label='History'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Machine = self.dboee.define_table('tblOee_Machine', \
                       Field('fldOeeMachineTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineNr', 'integer', label='Machine nr'), \
                       Field('fldOeeMachineCode', 'integer', label='Machine code'), \
                       Field('fldOeeModuleID', 'integer', label='Module'), \
                       Field('fldOeeMachineShortBreakID', 'integer', label='Shortbreak'), \
                       Field('fldOeeMachineUndefinedProdID', 'integer', label='Undefined Production'), \
                       Field('fldOeeMachineUndefinedStandStillID', 'integer', label='Undefined Standstill'), \
                       Field('fldOeeMachineUnscheduledID', 'integer', label='Unscheduled'), \
                       Field('fldOeeMachineIOFailureID', 'integer', label='I/O failure'), \
                       Field('fldOeeMachineUnitID', 'integer', label='Machine-unit'), \
                       Field('fldOeeMachineDescription', 'string', label='Machine description'), \
                       Field('fldOeeMachineInformation', 'string', label='Machine information'), \
                       Field('fldOeeMachineSortOrder', 'integer', label='Machine sort order'), \
                       Field('fldOeeMachineProductionBoundaryTimer', 'integer', label='Production timer'), \
                       Field('fldOeeMachineProductionShortbreakTimer', 'integer', label='Shortbreak timer'), \
                       Field('fldOeeMachineStopCodeTimer', 'integer', label='Stopcode timer'), \
                       Field('fldOeeMachineSpeed', 'integer', label='Default speed'), \
                       Field('fldOeeMachineDevider', 'decimal(2,2)', label='Pulse factor'), \
                       Field('fldOeeMachineOperatorFactor', 'decimal(2,2)', label='Operator factor'), \
                       Field('fldOeeMachineTarget1OEE', 'integer', label='OEE target 1'), \
                       Field('fldOeeMachineTarget2OEE', 'integer', label='OEE target 2'), \
                       Field('fldOeeMachineWorkstationDescription', 'string', label='Workstation description'), \
                       Field('fldOeeMachineHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_MachineActivity = self.dboee.define_table('tblOee_MachineActivity', \
                       Field('fldOeeMachineActivityTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineActivityID', 'integer', label='Activity'), \
                       Field('fldOeeMachineID', 'integer', label='Machine'), \
                       Field('fldOeeMachineActivitySortOrder', 'integer', label='Sort order'), \
                       Field('fldOeeMachineActivityHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_DailySchedule = self.dboee.define_table('tblOee_DailySchedule', \
                       Field('fldOeeDailyScheduleTableKeyID', 'id', readable=False), \
                       Field('fldOeeDailyScheduleNr', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID', 'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeTeamID', 'integer'), \
                       Field('fldOeeShiftTimeID', 'integer'), \
                       Field('fldOeeDailyScheduleDescription', 'string'), \
                       Field('fldOeeDailyScheduleInformation', 'string'), \
                       Field('fldOeeDailyScheduleStartDate', 'datetime'), \
                       Field('fldOeeDailyScheduleEndDate', 'datetime'), \
                       Field('fldOeeDailyScheduleHistory', 'boolean'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Article = self.dboee.define_table('tblOee_Article', \
                       Field('fldOeeArticleTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeArticleNr', 'string', label='Article nr'), \
                       Field('fldOeeArticleDescription', 'string', label='Article description'), \
                       Field('fldOeeArticleInformation', 'string', label='Article information'), \
                       Field('fldOeeArticleNormSpeed', 'integer', label='Norm speed'), \
                       Field('fldOeeArticleHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Order = self.dboee.define_table('tblOee_Order', \
                       Field('fldOeeOrderTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeArticleID', 'string', label='Article'), \
                       Field('fldOeeOrderNr', 'string', label='Order nr'), \
                       Field('fldOeeOrderDescription', 'string', label='Order description'), \
                       Field('fldOeeOrderInformation', 'string', label='Order information'), \
                       Field('fldOeeOrderHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_ShiftTime = self.dboee.define_table('tblOee_ShiftTime', \
                       Field('fldOeeShiftTimeTableKeyID', 'id'), \
                       Field('fldOeeShiftTimeNr', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeShiftTimeDescription', 'string'), \
                       Field('fldOeeShiftTimeInformation', 'string'), \
                       Field('fldOeeShiftTimeStart', 'datetime'), \
                       Field('fldOeeShiftTimeEnd', 'datetime'), \
                       Field('fldOeeShiftTimeHistory', 'boolean'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Team = self.dboee.define_table('tblOee_Team', \
                       Field('fldOeeTeamTableKeyID', 'id'), \
                       Field('fldOeeTeamNr', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeTeamDescription', 'string'), \
                       Field('fldOeeTeamInformation', 'string'), \
                       Field('fldOeeTeamColorNr', 'integer'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Reg = self.dboee.define_table('tblOee_Reg', \
                       Field('fldOeeRegTableKeyID', 'id', readable=False), \
                       Field('fldOeeRegNr', 'integer', label='Reg nr'), \
                       Field('fldOeeMachineCode', 'integer', label='Machine code'), \
                       Field('fldOeeMachineID', 'integer', label='Machine ID'), \
                       Field('fldOeeMachineDescription', 'string', label='Machine'), \
                       Field('fldOeeMachineStatusID', 'integer', label='Machine status ID'), \
                       Field('fldOeeMachineStatusDescription', 'string', label='Machine status description'), \
                       Field('fldOeeCountryID', 'integer', label='Country ID'), \
                       Field('fldOeeCountryDescription', 'string', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant ID'), \
                       Field('fldOeePlantDescription', 'string', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant ID'), \
                       Field('fldOeeSubPlantDescription', 'string', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department ID'), \
                       Field('fldOeeDepartmentDescription', 'string', label='Department'), \
                       Field('fldOeeStartDateTime', 'datetime', label='Start date'), \
                       Field('fldOeeEndDateTime', 'datetime', label='End date'), \
                       Field('fldOeeActivityDuration', 'integer', label='Duration'), \
                       Field('fldOeeTeamID', 'integer', label='Team ID'), \
                       Field('fldOeeTeamDescription', 'string', label='Team'), \
                       Field('fldOeeTeamColorID', 'integer', label='Team color ID'), \
                       Field('fldOeeTeamColorDescription', 'string', label='Team color'), \
                       Field('fldOeeShiftTimeID', 'integer', label='Shift ID'), \
                       Field('fldOeeShiftTimeDescription', 'string', label='Shift'), \
                       Field('fldOeeShiftStartDateTime', 'datetime', label='Shift starttime'), \
                       Field('fldOeeShiftEndDateTime', 'datetime', label='Shift endtime'), \
                       Field('fldOeeShiftDuration', 'integer', label='Shift duration'), \
                       Field('fldOeeAverageSpeed', 'integer', label='Average speed'), \
                       Field('fldOeeNormSpeed', 'integer', label='Norm speed'), \
                       Field('fldOeeCounter', 'integer', label='Counter'), \
                       Field('fldOeeCounterUnitID', 'integer', label='Counter-unit ID'), \
                       Field('fldOeeCounterUnitDescription', 'string', label='Counter-unit'), \
                       Field('fldOeeActivityGroupID', 'integer', label='Activitygroup ID'), \
                       Field('fldOeeActivityGroupDescription', 'string', label='Activitygroup'), \
                       Field('fldOeeActivityID', 'integer', label='Activity ID'), \
                       Field('fldOeeActivityDescription', 'string', label='Activity'), \
                       Field('fldOeeArticleNr', 'string', label='Article nr'), \
                       Field('fldOeeArticleDescription', 'string', label='Article description'), \
                       Field('fldOeeOrderNr', 'string', label='Order nr'), \
                       Field('fldOeeOrderDescription', 'string', label='Order description'), \
                       Field('fldOeeUserLogInformation', 'string', label='Activity log'), \
                       Field('fldOeeUserShiftLogInformation', 'string', label='Shift log'), \
                       Field('fldOeeCurrentPerformance', 'integer', label='Performance'), \
                       Field('fldOeeCurrentAvailability', 'integer', label='Availability'), \
                       Field('fldOeeCurrentQuality', 'integer', label='Quality'), \
                       Field('fldOeeCurrentOee', 'integer', label='OEE'), \
                       Field('fldOeeActivityGroupCalcForOee', 'integer', label='Calculate for OEE'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified'), \
                       Field('fldOeeSyncDate', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

        self.tblOee_Progress = self.dboee.define_table('tblOee_Progress', \
                       Field('fldOeeProgressTableKeyID', 'id'), \
                       Field('fldOeeRegID', 'integer'), \
                       Field('fldOeeStartDateTime', 'datetime'), \
                       Field('fldOeeActivityDuration', 'integer'), \
                       Field('fldOeeCounter', 'integer'), \
                       Field('fldOeeNormSpeed', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID',  'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeCurrentOee', 'integer'), \
                       Field('fldOeeCurrentAvailability', 'integer'), \
                       Field('fldOeeCurrentPerformance', 'integer'), \
                       Field('fldOeeCurrentQuality', 'integer'), \
                       Field('fldOeeRegHistory', 'boolean'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeMachineID', 'integer'), \
                       Field('fldOeeSyncDate', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))

    def dblocal(self):
        strWSName = str(self.request.vars['wsname'])
        row = self.dboee(self.dboee.tblOee_Machine.fldOeeMachineWorkstationDescription == strWSName).select()
        intMachineID = row[0].fldOeeMachineNr
        intCountryNr = row[0].fldOeeCountryID
        intPlantNr = row[0].fldOeePlantID
        intSubPlantNr = row[0].fldOeeSubPlantID
        intDepartmentNr = row[0].fldOeeDepartmentID

        strRandom = str(randint(0,999))
        dboee77 = DAL('sqlite://oee7' + strRandom + '7.db', pool_size=10)

        rows = self.dboee(self.dboee.tblOee_Country.fldOeeCountryNr == intCountryNr).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Country', \
                       Field('fldOeeCountryTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryNr', 'integer', label='Country nr', readable=False, writable=False), \
                       Field('fldOeeCountryDescription', 'string', label='Country description'), \
                       Field('fldOeeCountryInformation', 'string', label='Country information'), \
                       Field('fldOeeCountryLanguageID', 'integer', label='Language ID', readable=False, writable=False), \
                       Field('fldOeeCountryHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Country.fldOeeCountryTableKeyID > 0).delete()
        dboee77.tblOee_Country.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Plant.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Plant.fldOeePlantNr == intPlantNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Plant', \
                       Field('fldOeePlantTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country', readable=False, writable=False), \
                       Field('fldOeePlantNr', 'integer', label='Plant nr', readable=False, writable=False), \
                       Field('fldOeePlantDescription', 'string', label='Plant description'), \
                       Field('fldOeePlantInformation', 'string', label='Plant information'), \
                       Field('fldOeePlantHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Plant.fldOeePlantTableKeyID > 0).delete()
        dboee77.tblOee_Plant.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_SubPlant.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_SubPlant.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_SubPlant.fldOeeSubPlantNr == intSubPlantNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_SubPlant', \
                       Field('fldOeeSubPlantTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country', readable=False, writable=False), \
                       Field('fldOeePlantID', 'integer', label='Plant', readable=False, writable=False), \
                       Field('fldOeeSubPlantNr', 'integer', label='Sub-Plant nr', readable=False, writable=False), \
                       Field('fldOeeSubPlantDescription', 'string', label='Sub-Plant description'), \
                       Field('fldOeeSubPlantInformation', 'string', label='Sub-Plant information'), \
                       Field('fldOeeSubPlantHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_SubPlant.fldOeeSubPlantTableKeyID > 0).delete()
        dboee77.tblOee_SubPlant.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Department.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Department.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Department.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Department.fldOeeDepartmentNr == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Department', \
                       Field('fldOeeDepartmentTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country', readable=False, writable=False), \
                       Field('fldOeePlantID', 'integer', label='Plant', readable=False, writable=False), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant', readable=False, writable=False), \
                       Field('fldOeeDepartmentNr', 'integer', label='Department nr', readable=False, writable=False), \
                       Field('fldOeeDepartmentDescription', 'string', label='Department department'), \
                       Field('fldOeeDepartmentInformation', 'string', label='Department information'), \
                       Field('fldOeeDepartmentHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Department.fldOeeDepartmentTableKeyID > 0).delete()
        dboee77.tblOee_Department.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_ActivityGroup.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_ActivityGroup.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_ActivityGroup.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_ActivityGroup.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_ActivityGroup', \
                       Field('fldOeeActivityGroupTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeActivityGroupNr', 'integer', label='Activitygroup'), \
                       Field('fldOeeActivityGroupDescription', 'text', label='Activitygroup description'), \
                       Field('fldOeeActivityGroupInformation', 'text', label='Activitygroup information'), \
                       Field('fldOeeActivityGroupColorNr', 'integer', label='Activitygroup color'), \
                       Field('fldOeeActivityGroupCalcForOee', 'integer', label='Calculate OEE'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_ActivityGroup.fldOeeActivityGroupTableKeyID > 0).delete()
        dboee77.tblOee_ActivityGroup.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Activity.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Activity.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Activity.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Activity.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Activity', \
                       Field('fldOeeActivityTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeActivityNr', 'integer', label='Activity nr'), \
                       Field('fldOeeActivityGroupID', 'integer', label='Activitygroup'), \
                       Field('fldOeeActivityDescription', 'string', label='Activity description'), \
                       Field('fldOeeActivityInformation', 'string', label='Activity information'), \
                       Field('fldOeeActivityHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Activity.fldOeeActivityTableKeyID > 0).delete()
        dboee77.tblOee_Activity.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_ModuleSensorStyle.fldOeeCountryID == intCountryNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_ModuleSensorStyle', \
                       Field('fldOeeModuleSensorStyleTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeeModuleSensorStyleNr', 'integer', label='Sensor-style nr'), \
                       Field('fldOeeModuleSensorStyleDescription', 'string', label='Sensor-style'), \
                       Field('fldOeeModuleSensorStyleInformation', 'string', label='Sensor-style information'), \
                       Field('fldOeeModuleSensorStyleHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_ModuleSensorStyle.fldOeeModuleSensorStyleTableKeyID > 0).delete()
        dboee77.tblOee_ModuleSensorStyle.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_ModuleType.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_ModuleType.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_ModuleType.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_ModuleType.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_ModuleType', \
                       Field('fldOeeModuleTypeTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeModuleTypeNr', 'integer', label='Module-type nr'), \
                       Field('fldOeeModuleTypeConnection', 'string', label='Connection-type'), \
                       Field('fldOeeModuleTypeDescription', 'string', label='Module-type description'), \
                       Field('fldOeeModuleTypeInformation', 'string', label='Connection-type information'), \
                       Field('fldOeeModuleTypeHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_ModuleType.fldOeeModuleTypeTableKeyID > 0).delete()
        dboee77.tblOee_ModuleType.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Module.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Module.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Module.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Module.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Module', \
                       Field('fldOeeModuleTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeModuleNr', 'integer', label='Module nr'), \
                       Field('fldOeeModuleTypeID', 'integer', label='Module-type'), \
                       Field('fldOeeModuleSensorStyleID', 'integer', label='Sensor-style'), \
                       Field('fldOeeModuleDescription', 'string', label='Module description'), \
                       Field('fldOeeModuleInformation', 'string', label='Module information'), \
                       Field('fldOeeModuleIpAddress', 'string', label='IP address'), \
                       Field('fldOeeModuleIpAddressPort', 'integer', label='IP Port'), \
                       Field('fldOeeModuleComPort', 'string', label='Com port'), \
                       Field('fldOeeModuleBitsPerSecond', 'integer', label='Bits per Second'), \
                       Field('fldOeeModuleDatabits', 'integer', label='Databits'), \
                       Field('fldOeeModuleStopBits', 'integer', label='StopBits'), \
                       Field('fldOeeModuleFlowControl', 'string', label='Flowcontrol'), \
                       Field('fldOeeModuleSensorAddress', 'integer', label='Sensor address'), \
                       Field('fldOeeModuleSensorResetAddress', 'integer', label='Sensor reset address'), \
                       Field('fldOeeModuleParity', 'string', label='Parity'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeModuleHistory', 'boolean', label='History'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Module.fldOeeModuleTableKeyID > 0).delete()
        dboee77.tblOee_Module.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineIOFailure.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineIOFailure.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineIOFailure.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineIOFailure.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineIOFailure', \
                       Field('fldOeeMachineIOFailureTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineIOFailureNr', 'integer', label='I/O failure nr'), \
                       Field('fldOeeMachineIOFailureDescription', 'string', label='I/O failure'), \
                       Field('fldOeeMachineIOFailureInformation', 'string', label='I/O failure information'), \
                       Field('fldOeeMachineIOFailureHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineIOFailure.fldOeeMachineIOFailureTableKeyID > 0).delete()
        dboee77.tblOee_MachineIOFailure.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineShortbreak.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineShortbreak.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineShortbreak.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineShortbreak.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineShortbreak', \
                       Field('fldOeeMachineShortBreakTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineShortBreakNr', 'integer', label='Shortbreak nr'), \
                       Field('fldOeeMachineShortBreakDescription', 'string', label='Shortbreak description'), \
                       Field('fldOeeMachineShortBreakInformation', 'string', label='Shortbreak information'), \
                       Field('fldOeeMachineShortBreakHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineShortbreak.fldOeeMachineShortBreakTableKeyID > 0).delete()
        dboee77.tblOee_MachineShortbreak.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineStatus.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineStatus.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineStatus.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineStatus.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineStatus', \
                       Field('fldOeeMachineStatusTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineStatusNr', 'integer', label='Machine status nr'), \
                       Field('fldOeeMachineStatusDescription', 'string', label='Machine status description'), \
                       Field('fldOeeMachineStatusInformation', 'string', label='Machine status information'), \
                       Field('fldOeeMachineStatusHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineStatus.fldOeeMachineStatusTableKeyID > 0).delete()
        dboee77.tblOee_MachineStatus.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineUndefinedProduction.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineUndefinedProduction.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineUndefinedProduction.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineUndefinedProduction.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineUndefinedProduction', \
                       Field('fldOeeMachineUndefinedProductionTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUndefinedProductionNr', 'integer', label='Undefined Production nr'), \
                       Field('fldOeeMachineUndefinedProductionDescription', 'string', label='Undefined Production description'), \
                       Field('fldOeeMachineUndefinedProductionInformation', 'string', label='Undefined Production information'), \
                       Field('fldOeeMachineUndefinedProductionHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineUndefinedProduction.fldOeeMachineUndefinedProductionTableKeyID > 0).delete()
        dboee77.tblOee_MachineUndefinedProduction.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineUndefinedStandstill.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineUndefinedStandstill.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineUndefinedStandstill.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineUndefinedStandstill.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineUndefinedStandstill', \
                       Field('fldOeeMachineUndefinedStandstillTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUndefinedStandstillNr', 'integer', label='Undefined standstill nr'), \
                       Field('fldOeeMachineUndefinedStandstillDescription', 'string', label='Undefined standstill description'), \
                       Field('fldOeeMachineUndefinedStandstillInformation', 'string', label='Undefined standstill information'), \
                       Field('fldOeeMachineUndefinedStandstillHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineUndefinedStandstill.fldOeeMachineUndefinedStandstillTableKeyID > 0).delete()
        dboee77.tblOee_MachineUndefinedStandstill.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineUnscheduled.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineUnscheduled.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineUnscheduled.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineUnscheduled.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineUnscheduled', \
                       Field('fldOeeMachineUnscheduledTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUnscheduledNr', 'integer', label='Unscheduled nr'), \
                       Field('fldOeeMachineUnscheduledDescription', 'string', label='Unscheduled description'), \
                       Field('fldOeeMachineUnscheduledInformation', 'string', label='Unscheduled information'), \
                       Field('fldDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeMachineUnscheduledHistory', 'boolean', label='History'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineUnscheduled.fldOeeMachineUnscheduledTableKeyID > 0).delete()
        dboee77.tblOee_MachineUnscheduled.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineUnit.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineUnit.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineUnit.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineUnit.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineUnit', \
                       Field('fldOeeMachineUnitTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineUnitNr', 'integer', label='Machine-unit nr'), \
                       Field('fldOeeMachineUnitDescription', 'string', label='Machine-unit description'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeMachineUnitHistory', 'boolean', label='History'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineUnit.fldOeeMachineUnitTableKeyID > 0).delete()
        dboee77.tblOee_MachineUnit.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Machine.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Machine.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Machine.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Machine.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Machine', \
                       Field('fldOeeMachineTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineNr', 'integer', label='Machine nr'), \
                       Field('fldOeeMachineCode', 'integer', label='Machine code'), \
                       Field('fldOeeModuleID', 'integer', label='Module'), \
                       Field('fldOeeMachineShortBreakID', 'integer', label='Shortbreak'), \
                       Field('fldOeeMachineUndefinedProdID', 'integer', label='Undefined Production'), \
                       Field('fldOeeMachineUndefinedStandStillID', 'integer', label='Undefined Standstill'), \
                       Field('fldOeeMachineUnscheduledID', 'integer', label='Unscheduled'), \
                       Field('fldOeeMachineIOFailureID', 'integer', label='I/O failure'), \
                       Field('fldOeeMachineUnitID', 'integer', label='Machine-unit'), \
                       Field('fldOeeMachineDescription', 'string', label='Machine description'), \
                       Field('fldOeeMachineInformation', 'string', label='Machine information'), \
                       Field('fldOeeMachineSortOrder', 'integer', label='Machine sort order'), \
                       Field('fldOeeMachineProductionBoundaryTimer', 'integer', label='Production timer'), \
                       Field('fldOeeMachineProductionShortbreakTimer', 'integer', label='Shortbreak timer'), \
                       Field('fldOeeMachineStopCodeTimer', 'integer', label='Stopcode timer'), \
                       Field('fldOeeMachineSpeed', 'integer', label='Default speed'), \
                       Field('fldOeeMachineDevider', 'decimal(2,2)', label='Pulse factor'), \
                       Field('fldOeeMachineOperatorFactor', 'decimal(2,2)', label='Operator factor'), \
                       Field('fldOeeMachineTarget1OEE', 'integer', label='OEE target 1'), \
                       Field('fldOeeMachineTarget2OEE', 'integer', label='OEE target 2'), \
                       Field('fldOeeMachineWorkstationDescription', 'string', label='Workstation description'), \
                       Field('fldOeeMachineHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Machine.fldOeeMachineTableKeyID > 0).delete()
        dboee77.tblOee_Machine.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_MachineActivity.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_MachineActivity.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_MachineActivity.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_MachineActivity.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_MachineActivity', \
                       Field('fldOeeMachineActivityTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeMachineActivityID', 'integer', label='Activity'), \
                       Field('fldOeeMachineID', 'integer', label='Machine'), \
                       Field('fldOeeMachineActivitySortOrder', 'integer', label='Sort order'), \
                       Field('fldOeeMachineActivityHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_MachineActivity.fldOeeMachineActivityTableKeyID > 0).delete()
        dboee77.tblOee_MachineActivity.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_DailySchedule.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_DailySchedule.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_DailySchedule.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_DailySchedule.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_DailySchedule', \
                       Field('fldOeeDailyScheduleTableKeyID', 'id', readable=False), \
                       Field('fldOeeDailyScheduleNr', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID', 'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeTeamID', 'integer'), \
                       Field('fldOeeShiftTimeID', 'integer'), \
                       Field('fldOeeDailyScheduleDescription', 'string'), \
                       Field('fldOeeDailyScheduleInformation', 'string'), \
                       Field('fldOeeDailyScheduleStartDate', 'datetime'), \
                       Field('fldOeeDailyScheduleEndDate', 'datetime'), \
                       Field('fldOeeDailyScheduleHistory', 'boolean'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_DailySchedule.fldOeeDailyScheduleTableKeyID > 0).delete()
        dboee77.tblOee_DailySchedule.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Article.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Article.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Article.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Article.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Article', \
                       Field('fldOeeArticleTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeArticleNr', 'string', label='Article nr'), \
                       Field('fldOeeArticleDescription', 'string', label='Article description'), \
                       Field('fldOeeArticleInformation', 'string', label='Article information'), \
                       Field('fldOeeArticleNormSpeed', 'integer', label='Norm speed'), \
                       Field('fldOeeArticleHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Article.fldOeeArticleTableKeyID > 0).delete()
        dboee77.tblOee_Article.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Order.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Order.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Order.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Order.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Order', \
                       Field('fldOeeOrderTableKeyID', 'id', readable=False), \
                       Field('fldOeeCountryID', 'integer', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department'), \
                       Field('fldOeeArticleID', 'string', label='Article'), \
                       Field('fldOeeOrderNr', 'string', label='Order nr'), \
                       Field('fldOeeOrderDescription', 'string', label='Order description'), \
                       Field('fldOeeOrderInformation', 'string', label='Order information'), \
                       Field('fldOeeOrderHistory', 'boolean', label='History'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified', default = self.request.now), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Order.fldOeeOrderTableKeyID > 0).delete()
        dboee77.tblOee_Order.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_ShiftTime.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_ShiftTime.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_ShiftTime.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_ShiftTime.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_ShiftTime', \
                       Field('fldOeeShiftTimeTableKeyID', 'id'), \
                       Field('fldOeeShiftTimeNr', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeShiftTimeDescription', 'string'), \
                       Field('fldOeeShiftTimeInformation', 'string'), \
                       Field('fldOeeShiftTimeStart', 'datetime'), \
                       Field('fldOeeShiftTimeEnd', 'datetime'), \
                       Field('fldOeeShiftTimeHistory', 'boolean'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_ShiftTime.fldOeeShiftTimeTableKeyID > 0).delete()
        dboee77.tblOee_ShiftTime.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Team.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Team.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Team.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Team.fldOeeDepartmentID == intDepartmentNr)).select()
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Team', \
                       Field('fldOeeTeamTableKeyID', 'id'), \
                       Field('fldOeeTeamNr', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeTeamDescription', 'string'), \
                       Field('fldOeeTeamInformation', 'string'), \
                       Field('fldOeeTeamColorNr', 'integer'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Team.fldOeeTeamTableKeyID > 0).delete()
        dboee77.tblOee_Team.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Reg.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Reg.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Reg.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Reg.fldOeeDepartmentID == intDepartmentNr)).select(self.dboee.tblOee_Reg.ALL, \
                                              orderby=~self.dboee.tblOee_Reg.fldOeeRegTableKeyID, \
                                              limitby=(0,1))
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Reg', \
                       Field('fldOeeRegTableKeyID', 'id', readable=False), \
                       Field('fldOeeRegNr', 'integer', label='Reg nr'), \
                       Field('fldOeeMachineCode', 'integer', label='Machine code'), \
                       Field('fldOeeMachineID', 'integer', label='Machine ID'), \
                       Field('fldOeeMachineDescription', 'string', label='Machine'), \
                       Field('fldOeeMachineStatusID', 'string', label='Machine status ID'), \
                       Field('fldOeeMachineStatusDescription', 'string', label='Machine status description'), \
                       Field('fldOeeCountryID', 'integer', label='Country ID'), \
                       Field('fldOeeCountryDescription', 'string', label='Country'), \
                       Field('fldOeePlantID', 'integer', label='Plant ID'), \
                       Field('fldOeePlantDescription', 'string', label='Plant'), \
                       Field('fldOeeSubPlantID', 'integer', label='Sub-Plant ID'), \
                       Field('fldOeeSubPlantDescription', 'string', label='Sub-Plant'), \
                       Field('fldOeeDepartmentID', 'integer', label='Department ID'), \
                       Field('fldOeeDepartmentDescription', 'string', label='Department'), \
                       Field('fldOeeStartDateTime', 'datetime', label='Start date'), \
                       Field('fldOeeEndDateTime', 'datetime', label='End date'), \
                       Field('fldOeeActivityDuration', 'integer', label='Duration'), \
                       Field('fldOeeTeamID', 'integer', label='Team ID'), \
                       Field('fldOeeTeamDescription', 'string', label='Team'), \
                       Field('fldOeeTeamColorID', 'integer', label='Team color ID'), \
                       Field('fldOeeTeamColorDescription', 'string', label='Team color'), \
                       Field('fldOeeShiftTimeID', 'integer', label='Shift ID'), \
                       Field('fldOeeShiftTimeDescription', 'string', label='Shift'), \
                       Field('fldOeeShiftStartDateTime', 'datetime', label='Shift starttime'), \
                       Field('fldOeeShiftEndDateTime', 'datetime', label='Shift endtime'), \
                       Field('fldOeeShiftDuration', 'integer', label='Shift duration'), \
                       Field('fldOeeAverageSpeed', 'integer', label='Average speed'), \
                       Field('fldOeeNormSpeed', 'integer', label='Norm speed'), \
                       Field('fldOeeCounter', 'integer', label='Counter'), \
                       Field('fldOeeCounterUnitID', 'integer', label='Counter-unit ID'), \
                       Field('fldOeeCounterUnitDescription', 'string', label='Counter-unit'), \
                       Field('fldOeeActivityGroupID', 'integer', label='Activitygroup ID'), \
                       Field('fldOeeActivityGroupDescription', 'string', label='Activitygroup'), \
                       Field('fldOeeActivityID', 'integer', label='Activity ID'), \
                       Field('fldOeeActivityDescription', 'string', label='Activity'), \
                       Field('fldOeeArticleNr', 'string', label='Article nr'), \
                       Field('fldOeeArticleDescription', 'string', label='Article description'), \
                       Field('fldOeeOrderNr', 'string', label='Order nr'), \
                       Field('fldOeeOrderDescription', 'string', label='Order description'), \
                       Field('fldOeeUserLogInformation', 'string', label='Activity log'), \
                       Field('fldOeeUserShiftLogInformation', 'string', label='Shift log'), \
                       Field('fldOeeCurrentPerformance', 'integer', label='Performance'), \
                       Field('fldOeeCurrentAvailability', 'integer', label='Availability'), \
                       Field('fldOeeCurrentQuality', 'integer', label='Quality'), \
                       Field('fldOeeCurrentOee', 'integer', label='OEE'), \
                       Field('fldOeeActivityGroupCalcForOee', 'integer', label='Calculate for OEE'), \
                       Field('fldOeeDateModified', 'datetime', label='Date modified'), \
                       Field('fldOeeSyncDate', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Reg.fldOeeRegTableKeyID > 0).delete()
        dboee77.tblOee_Reg.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()

        rows = self.dboee((self.dboee.tblOee_Progress.fldOeeCountryID == intCountryNr) & \
                     (self.dboee.tblOee_Progress.fldOeePlantID == intPlantNr) & \
                     (self.dboee.tblOee_Progress.fldOeeSubPlantID == intSubPlantNr) & \
                     (self.dboee.tblOee_Progress.fldOeeDepartmentID == intDepartmentNr)).select(self.dboee.tblOee_Progress.ALL, \
                                                                                           limitby=(0,0))
        rows.export_to_csv_file(open('oee' + strRandom + '.csv', 'wb'))
        dboee77.define_table('tblOee_Progress', \
                       Field('fldOeeProgressTableKeyID', 'id'), \
                       Field('fldOeeRegID', 'integer'), \
                       Field('fldOeeStartDateTime', 'datetime'), \
                       Field('fldOeeActivityDuration', 'integer'), \
                       Field('fldOeeCounter', 'integer'), \
                       Field('fldOeeNormSpeed', 'integer'), \
                       Field('fldOeeCountryID', 'integer'), \
                       Field('fldOeePlantID', 'integer'), \
                       Field('fldOeeSubPlantID',  'integer'), \
                       Field('fldOeeDepartmentID', 'integer'), \
                       Field('fldOeeCurrentOee', 'integer'), \
                       Field('fldOeeCurrentAvailability', 'integer'), \
                       Field('fldOeeCurrentPerformance', 'integer'), \
                       Field('fldOeeCurrentQuality', 'integer'), \
                       Field('fldOeeRegHistory', 'boolean'), \
                       Field('fldOeeDateModified', 'datetime'), \
                       Field('fldOeeMachineID', 'integer'), \
                       Field('fldOeeSyncDate', 'datetime'), \
                       Field('fldOeeSync', 'boolean', label='Sync', default = True))
        dboee77(dboee77.tblOee_Progress.fldOeeProgressTableKeyID > 0).delete()
        dboee77.tblOee_Progress.import_from_csv_file(open('oee' + strRandom + '.csv', 'r'))
        for row in rows:
            row.fldOeeSync = False
            row.update_record()
        return self.response.stream('applications/OEEWeb/databases/oee7' + strRandom + '7.db')
