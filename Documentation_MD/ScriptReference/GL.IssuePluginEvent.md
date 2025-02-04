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

#  [GL](GL.html).IssuePluginEvent

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

**Obsolete** IssuePluginEvent(eventID) is deprecated. Use
IssuePluginEvent(callback, eventID) instead.

## Declaration

public static void IssuePluginEvent(int eventID);

## Declaration

public static void IssuePluginEvent(IntPtr callback, int eventID);

### Parameters

eventID | User defined id to send to the callback.  
---|---  
callback | Native code callback to queue for Unity's renderer to invoke.  
  
### Description

Send a user-defined event to a native code plugin.

Rendering in Unity can be multithreaded if the platform and number of
available CPUs will allow for it. When multithreaded rendering is used, the
rendering API commands happen on a thread which is completely separate from
the one that runs the scripts. Consequently, it is not possible for your
plugin to start rendering immediately, since it might interfere with what the
render thread is doing at the time.  
  
In order to do any rendering from the plugin, you should call
GL.IssuePluginEvent from your script, which will cause your native plugin to
be called from the render thread. For example, if you call GL.IssuePluginEvent
from the camera's OnPostRender function, you'll get a plugin callback
immediately after the camera has finished rendering.  
  
Callback must be a native function of "void UNITY_INTERFACE_API
UnityRenderingEvent(int eventId)" signature.  
  
See [Native Plugin Interface](../Manual/native-plugin-interface.html) for more
details and an example.  
  
Additional resources: [SystemInfo.graphicsMultiThreaded](SystemInfo-
graphicsMultiThreaded.html).

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

