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

#  [ParticleSystem](ParticleSystem.html).SetMaximumPreMappedBufferCounts

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

## Declaration

public static void SetMaximumPreMappedBufferCounts(int vertexBuffersCount, int
indexBuffersCount);

### Parameters

vertexBuffersCount | The maximum number of cached vertex buffers.  
---|---  
indexBuffersCount | The maximum number of cached index buffers.  
  
### Description

Limits the amount of graphics memory Unity reserves for efficient rendering of
Particle Systems.

To efficiently write particle data into graphics memory, Unity uses a pool of
pre-allocated vertex buffers. When rendering a large number of particles, this
pool will increase in size. If the number of particles decreases later, the
pool still maintains this size.  
  
Maintaining a large pool can make future rendering more efficient, in
situations where a large number of particles are being rendered, and the pool
is already pre-sized appropriately. However, a large pool uses more memory, so
this function allows you to set a limit on the number of buffers in the cache.  
  
If the total number of visible particles reaches the limit, Unity allocates
new buffers and releases them on-demand within the frames that need them,
rather than saving them for re-use on multiple frames. This can be slower but
prevents the cache from using too much memory.  
  
Modern graphics APIs, such as DirectX12, Vulkan and Metal, do not use a pre-
allocated pool of vertex buffers, because they can operate efficiently without
it. This method does nothing on these devices.

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

