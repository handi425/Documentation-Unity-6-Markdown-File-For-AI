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

#  [AudioSource](AudioSource.html).panStereo

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

[Switch to Manual](../Manual/class-AudioSource.html "Go to AudioSource
Component in the Manual")

public float panStereo;

### Description

Pans a playing sound in a stereo way (left or right). This only applies to
sounds that are Mono or Stereo.

This pan is applied before 3D panning calculations are considered. In other
words, stereo panning affects the left right balance of the sound before it is
spatialised in 3D.  
  
Mono sounds are panned from left to right using constant power panning (non
linear fade). This means when pan = 0.0, the balance for the sound in each
speaker is 71% left and 71% right, not 50% left and 50% right. This gives
(audibly) smoother pans.  
  
Stereo sounds heave each left/right value faded up and down according to the
specified pan position. This means when pan = 0.0, the balance for the sound
in each speaker is 100% left and 100% right. When pan = -1.0, only the left
channel of the stereo sound is audible, when pan = 1.0, only the right channel
of the stereo sound is audible.  
  
Values range from -1.0 to 1.0.  
  
-1.0 = Full left 0.0 = center 1.0 = full right  
  
Default = 0.0.

    
    
    no example available in C#

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

