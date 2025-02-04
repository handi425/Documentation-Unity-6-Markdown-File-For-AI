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

**Experimental** : this API is experimental and might be changed or removed in
the future.

#
[AudioSampleProvider](Experimental.Audio.AudioSampleProvider.html).consumeSampleFramesNativeFunction

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

public static
[Experimental.Audio.AudioSampleProvider.ConsumeSampleFramesNativeFunction](Experimental.Audio.AudioSampleProvider.ConsumeSampleFramesNativeFunction.html)
consumeSampleFramesNativeFunction;

### Description

Pointer to the native function that provides access to audio sample frames.

This function pointer can be passed to native plug-ins that need to consume
sample frames while avoiding any overhead related to going from native to C#
or garbage collection interference.  
  
Importing a native function that uses this type, for passing the native
function pointer to the native plugin, would look like this:

    
    
    SetConsumeSampleFramesFunction(
        [AudioSampleProvider.consumeSampleFramesNativeFunction](Experimental.Audio.AudioSampleProvider-consumeSampleFramesNativeFunction.html), signalProvider.id,
        signalProvider.channelCount, signalProvider.sampleRate);
    

See
[ConsumeSampleFramesNativeFunction](Experimental.Audio.AudioSampleProvider.ConsumeSampleFramesNativeFunction.html)
for how to import a native function that uses this signature.

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

