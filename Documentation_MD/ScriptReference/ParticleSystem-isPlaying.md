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

#  [ParticleSystem](ParticleSystem.html).isPlaying

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

public bool isPlaying;

### Description

Determines whether the Particle System is playing.

[isPlaying](ParticleSystem-isPlaying.html) is `true` from when the Particle
System begins to play until its last live particle dies.
[isPlaying](ParticleSystem-isPlaying.html) is `false` when the Particle System
is no longer spawning particles and is not simulating any live particles.
(Read Only).

    
    
    using UnityEngine;  
      
    // A particle sprite example of isPlaying. A button is created
    // that shows whether the [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html) is running.  If not, then
    // it can be started.  If it is running then it can be stopped.  
      
    using UnityEngine;  
      
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
      
        void OnGUI()
        {
            if (ps.isPlaying)
            {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 70, 150, 50), "Stop and clear"))
                {
                    ps.Stop(true, [ParticleSystemStopBehavior.StopEmittingAndClear](ParticleSystemStopBehavior.StopEmittingAndClear.html));
                }
            }
            else
            {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 70, 150, 50), "Play"))
                {
                    ps.Play(false);
                }
            }
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

