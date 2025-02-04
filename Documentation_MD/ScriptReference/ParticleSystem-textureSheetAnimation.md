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

#  [ParticleSystem](ParticleSystem.html).textureSheetAnimation

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

public
[ParticleSystem.TextureSheetAnimationModule](ParticleSystem.TextureSheetAnimationModule.html)
textureSheetAnimation;

### Description

Script interface for the TextureSheetAnimationModule of a Particle System.

This module allows you to add animations to your particle textures. This is
achieved by authoring flipbook textures, which look like this:  
  
![](../StaticFiles/ScriptRefImages/ParticleFlipbook.png)  
  
Each numbered region represents a frame of the animation, and must be
distributed evenly across the texture. Select a variable below to see script
examples. You may want to use this texture on your Particle System with each
example, to see how the module works.  
  
Particle System modules do not need to be reassigned back to the system; they
are interfaces and not independent objects.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {
        void Start() {
            [ParticleSystem](ParticleSystem.html) ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var ts = ps.textureSheetAnimation;
                ts.enabled = true;
            ts.numTilesX = 2;
            ts.rowMode = [ParticleSystemAnimationRowMode.Random](ParticleSystemAnimationRowMode.Random.html);
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

