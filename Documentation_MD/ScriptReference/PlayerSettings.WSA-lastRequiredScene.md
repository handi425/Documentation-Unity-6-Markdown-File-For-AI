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

#  [PlayerSettings.WSA](PlayerSettings.WSA.html).lastRequiredScene

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

public static int lastRequiredScene;

### Description

The scene index number from the [Scenes in
Build](../Manual/BuildSettings.html) list for the last scene that must be
present in a **Streaming Install** build.

In the Editor, Unity displays this under **Packaging** in [UWP Player
Settings](../Manual/class-PlayerSettingsWSA.html).  
For an application to start, Unity requires all scenes in the Build Settings,
up to this index, to be present on the device. If your application requires
every scene in the list before the application can start, set this value to
the index of the last scene in the list (scene_count - 1).  
A scene may only use assets from another scene with a _smaller_ index value.
This means that the ordering of scenes within a streaming install is important
because it determines the order in which Unity installs. Your application
can't share assets in scenes lower down the list (larger index value) with
scenes higher in the list (smaller index value).  
  
**Note** : By default, Unity disables Streaming Install and ignores this
value. Set [supportStreamingInstall](PlayerSettings.WSA-
supportStreamingInstall.html) to `true` or check the **Streaming Install**
option in PlayerSettings to enable this feature.

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

