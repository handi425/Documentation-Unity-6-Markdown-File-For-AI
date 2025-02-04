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

#  [AudioListener](AudioListener.html).GetOutputData

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

[Switch to Manual](../Manual/class-AudioListener.html "Go to AudioListener
Component in the Manual")

## Declaration

public static void GetOutputData(float[] samples, int channel);

### Parameters

samples | The array to populate with audio samples. Its length must be a power of 2.  
---|---  
channel | The channel to sample from.  
  
### Description

Provides a block of the listener (master)'s output data.

The array given in the samples parameter will be filled with the requested
data.  
  
Additional resources:
[AudioListener.GetSpectrumData](AudioListener.GetSpectrumData.html),
[AudioSource.GetSpectrumData](AudioSource.GetSpectrumData.html),
[AudioSource.GetOutputData](AudioSource.GetOutputData.html).

* * *

**Obsolete** GetOutputData returning a float[] is deprecated, use
GetOutputData and pass a pre allocated array instead.

## Declaration

public static float[] GetOutputData(int numSamples, int channel);

### Description

_Deprecated Version_. Returns a block of the listener (master)'s output data.

This variation of the function allocates a new array each time it is called.
Use the Non-alloc version instead for better performance.

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

