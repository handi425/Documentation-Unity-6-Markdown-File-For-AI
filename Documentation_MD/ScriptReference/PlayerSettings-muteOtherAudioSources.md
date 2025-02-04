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

#  [PlayerSettings](PlayerSettings.html).muteOtherAudioSources

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

public static bool muteOtherAudioSources;

### Description

Stops or allows audio from other applications to play in the background while
your Unity application is running.

This setting is shared between iOS and Android platforms.  
  
Set this to true and your Unity application stops audio from other
applications in the background, set to false and audio from background
applications continues to play alongside your Unity application.  
  
Unity ignores `PlayerSettings.muteOtherAudioSources` if at least one of the
following is true:

  * Unity Audio is disabled. (menu: **Edit** > **Project Settings** > **Audio** > **Disable Unity Audio**)
  * Unity has stripped the AudioManager from the project at build time.

AudioManager is stripped from the project if all of the following are true:

  * There is no audio content in the project.
  * The project uses IL2CPP.
  * [Strip Engine Code](PlayerSettings-stripEngineCode.html) is enabled.

Note: Starting with Android Marshmallow (6.0), setting this to false mutes the
sound of your Unity application during an incoming phone call (while the phone
is ringing). If you want to have this behavior on older Android versions, you
have to add the READ_PHONE_STATE permission to the manifest. See [the Android
documentation](https://developer.android.com/guide/topics/manifest/manifest-
intro.html) for more information on build manifests.

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

