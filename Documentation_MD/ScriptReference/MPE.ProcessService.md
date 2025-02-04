[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# ProcessService

class in UnityEditor.MPE

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

*This is an experimental feature.* The ProcessService allows you to start slave instance of UnityEditor, opened to the same Project as the master instance, with a specific [RoleProviderAttribute](MPE.RoleProviderAttribute.html).

The Standalone Profiler workflow uses this technology.

### Static Properties

[level](MPE.ProcessService-level.html)| The ProcessLevel of the running
instance of UnityEditor.  
---|---  
[roleName](MPE.ProcessService-roleName.html)| The role name of the running
UnityEditor process. For more information about how to register handlers for a
specific process role, see RoleProviderAttribute. For a UnityEditor process of
ProcessLevel Master, the roleName is always empty.  
  
### Static Methods

[DisableProfileConnection](MPE.ProcessService.DisableProfileConnection.html)|
Closes the Profiler connection.  
---|---  
[EnableProfileConnection](MPE.ProcessService.EnableProfileConnection.html)|
Enables a connection to the Profiler. The standalone Profiler uses this
method.  
[GetProcessState](MPE.ProcessService.GetProcessState.html)| Gets the
ProcessState of a given instance of UnityEditor.  
[HasCapability](MPE.ProcessService.HasCapability.html)| Checks whether the
current process has a given capability.  
[IsChannelServiceStarted](MPE.ProcessService.IsChannelServiceStarted.html)|
Checks whether the ChannelService is already started.  
[Launch](MPE.ProcessService.Launch.html)| Launches a secondary instance of
UnityEditor on the same project as the master instance.  
[ReadParameter](MPE.ProcessService.ReadParameter.html)| A utility function to
read command line arguments passed to the current process.  
[Terminate](MPE.ProcessService.Terminate.html)| Terminates an editor process.  
  
### Events

[ProcessExitedEvent](MPE.ProcessService.ProcessExitedEvent.html)| An event
triggered in a master instance of UnityEditor when you start a slave instance
with ProcessService.Launch exit.  
---|---  
[SlaveProcessExitedEvent](MPE.ProcessService.SlaveProcessExitedEvent.html)| An
event triggered in a master instance of UnityEditor when you start a slave
instance with ProcessService.LaunchSlave exit.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

