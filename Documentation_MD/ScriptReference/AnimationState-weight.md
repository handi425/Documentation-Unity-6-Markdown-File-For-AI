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

#  [AnimationState](AnimationState.html).weight

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

public float weight;

### Description

The weight of animation.

This calculates the blend weights for one curve.  
  
Weights are distributed so that the top layer gets everything. If it doesn't
use the full weight then the next layer gets to distribute the remaining
weights and so on. Once all weights are used by the top layers, no weights
will be available for lower layers anymore Unity uses fair weighting, which
means if a lower layer wants 80% and 50% have already been used up, the layer
will NOT use up all weights. instead it will take up 80% of the 50%.  
  
**Example:** a upper body which is affected by wave, walk and idle a lower
body which is affected by only walk and idle.  
  
\- Blend weights can change per animated value because of mixing. Even without
mixing, sometimes a curve is just not defined. Still you want the blend
weights to add up to 1. Most of the time weights are similar between curves.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Animation](Animation.html) anim;  
      
        void Start()
        {
            // Set the blend weight of the walk animation to 0.5
            anim["Walk"].weight = 0.5f;
        }
    }
    

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

