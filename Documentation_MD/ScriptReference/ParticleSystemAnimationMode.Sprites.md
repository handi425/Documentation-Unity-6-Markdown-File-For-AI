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

#  [ParticleSystemAnimationMode](ParticleSystemAnimationMode.html).Sprites

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

### Description

Use a list of sprites to construct a sequence of animation frames.

Defines the sprites that are added to Texture Sheet Animation.  
  
Additional resources:
[ParticleSystemAnimationMode.Grid](ParticleSystemAnimationMode.Grid.html)

    
    
    using UnityEngine;  
      
    // A particle sprite example.
    // The gameobject this script is attached to must have the
    // [ParticleSystem](ParticleSystem.html) attached.  The TextureSheetAnimation mode
    // is set to Sprites.  This script adds a single texture to
    // the [ParticleSystem](ParticleSystem.html).  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture2D](Texture2D.html) tex;
        private [ParticleSystem](ParticleSystem.html) ps;
        private [Sprite](Sprite.html) sprite;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            sprite = [Sprite.Create](Sprite.Create.html)(tex, new [Rect](Rect.html)(0.0f, 0.0f, tex.width, tex.height), [Vector2.zero](Vector2-zero.html));  
      
            var textureSheetAnimation = ps.textureSheetAnimation;
            textureSheetAnimation.enabled = true;
            textureSheetAnimation.mode = [ParticleSystemAnimationMode.Sprites](ParticleSystemAnimationMode.Sprites.html);
            textureSheetAnimation.AddSprite(sprite);
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

