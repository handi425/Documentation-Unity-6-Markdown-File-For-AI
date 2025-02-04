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

#  [AudioSettings](AudioSettings.html).GetDSPBufferSize

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

[Switch to Manual](../Manual/class-AudioSettings.html "Go to AudioSettings
Component in the Manual")

## Declaration

public static void GetDSPBufferSize(out int bufferLength, out int numBuffers);

### Parameters

bufferLength | Is the length of each buffer in the ring buffer.  
---|---  
numBuffers | Is number of buffers.  
  
### Description

Get the mixer's buffer size in samples.

The buffer size can be set from 'Project Settings -> Audio -> DSP Buffer
size'.  
  
The software mixer mixes to a ring buffer and the size of this ring buffer is
determined here. It mixes a block of sound data every 'bufferLength' number of
samples, and there are 'numBuffers' number of these blocks that make up the
entire ring buffer. Adjusting these values can lead to extremely low latency
performance (smaller values), or greater stability in sound output (larger
values). The 'buffersize' is generally best left alone. Making the granularity
smaller will just increase CPU usage (cache misses and DSP network overhead).
Making it larger affects how often you hear commands update such as
volume/pitch/pan changes. Anything above 20 ms will be noticeable and sound
parameter changes will be obvious instead of smooth. Unity chooses the most
optimal size by default for best stability, considering the output type and
the drivers being used. It is not recommended changing this value unless you
really need to. You may get worse performance than the default settings chosen
by Unity.  
  
Additional resources: [Audio Settings](../Manual/class-AudioSettings.html).

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

