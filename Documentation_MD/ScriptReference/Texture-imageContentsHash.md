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

#  [Texture](Texture.html).imageContentsHash

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

public [Hash128](Hash128.html) imageContentsHash;

### Description

The hash value of the Texture.

Note: The hash is an Editor-only property.  
  
The hash value is a 128-bit number computed in such a way that even slightly
different Textures have different hash values. The principal use of the hash
in this case is to detect when the Texture has changed. Unity updates the hash
when changing or rendering into a Texture. Likewise, you must calculate a new
hash when modifying the Texture contents so that Unity knows when the Texture
changes. Changing the hash lets the Global Illumination system know that it
needs to recalculate maps in the Scene that are affected by the Texture.  
  
For regular Textures, Unity first computes the hash when the Texture is
imported into the Editor, and updates the hash after light and reflections are
"baked" into the Texture. If you subsequently render into a Texture which is
used as an input for the Global Illumination system (such as sky, light or
reflection probes), then you must update the Texture hash yourself.  
  
Using the pixel values of the Texture to calculate the hash might be
inefficient or impossible. A more efficient way of doing this is to hash the
input parameters of the code you used to create the Texture. Whatever method
you use, you must ensure that the resulting hash is different for different
Textures, and the same for the identical Textures.  
  
Additional resources: [Hash128.Compute](Hash128.Compute.html).

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

