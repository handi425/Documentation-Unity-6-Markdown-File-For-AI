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

# TextureSheetAnimationModule

struct in UnityEngine

/

Implemented
in:[UnityEngine.ParticleSystemModule](UnityEngine.ParticleSystemModule.html)

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

### Description

Script interface for the TextureSheetAnimationModule.

This module allows you to add animations to your particle textures. To author
an animation, you must use a flipbook Texture, which look like this:  
  
![](../StaticFiles/ScriptRefImages/ParticleFlipbook.png)  
  
Each numbered region represents a frame of the animation, which you must
distribute evenly across the Texture. Select a variable below to see script
examples. You may want to use this Texture on your Particle System with each
example, to see how the module works.  
  
Additional resources: [ParticleSystem](ParticleSystem.html),
[ParticleSystem.textureSheetAnimation](ParticleSystem-
textureSheetAnimation.html).

### Properties

[animation](ParticleSystem.TextureSheetAnimationModule-animation.html)|
Specifies the animation type.  
---|---  
[cycleCount](ParticleSystem.TextureSheetAnimationModule-cycleCount.html)|
Specifies how many times the animation loops during the lifetime of the
particle.  
[enabled](ParticleSystem.TextureSheetAnimationModule-enabled.html)| Specifies
whether the TextureSheetAnimationModule is enabled or disabled.  
[fps](ParticleSystem.TextureSheetAnimationModule-fps.html)| Control how
quickly the animation plays.  
[frameOverTime](ParticleSystem.TextureSheetAnimationModule-
frameOverTime.html)| A curve to control which frame of the Texture sheet
animation to play.  
[frameOverTimeMultiplier](ParticleSystem.TextureSheetAnimationModule-
frameOverTimeMultiplier.html)| The frame over time mutiplier.  
[mode](ParticleSystem.TextureSheetAnimationModule-mode.html)| Select whether
the animated Texture information comes from a grid of frames on a single
Texture, or from a list of Sprite objects.  
[numTilesX](ParticleSystem.TextureSheetAnimationModule-numTilesX.html)|
Defines the tiling of the Texture in the x-axis.  
[numTilesY](ParticleSystem.TextureSheetAnimationModule-numTilesY.html)|
Defines the tiling of the texture in the y-axis.  
[rowIndex](ParticleSystem.TextureSheetAnimationModule-rowIndex.html)|
Explicitly select which row of the Texture sheet to use. The system uses this
property when ParticleSystem.TextureSheetAnimationModule.rowMode is set to
Custom.  
[rowMode](ParticleSystem.TextureSheetAnimationModule-rowMode.html)| Select how
particles choose which row of a Texture Sheet Animation to use.  
[speedRange](ParticleSystem.TextureSheetAnimationModule-speedRange.html)|
Specify how particle speeds are mapped to the animation frames.  
[spriteCount](ParticleSystem.TextureSheetAnimationModule-spriteCount.html)|
The total number of sprites.  
[startFrame](ParticleSystem.TextureSheetAnimationModule-startFrame.html)|
Define a random starting frame for the Texture sheet animation.  
[startFrameMultiplier](ParticleSystem.TextureSheetAnimationModule-
startFrameMultiplier.html)| The starting frame multiplier.  
[timeMode](ParticleSystem.TextureSheetAnimationModule-timeMode.html)| Select
whether the system bases the playback on mapping a curve to the lifetime of
each particle, by using the particle speeds, or if playback simply uses a
constant frames per second.  
[uvChannelMask](ParticleSystem.TextureSheetAnimationModule-
uvChannelMask.html)| Choose which UV channels receive Texture animation.  
  
### Public Methods

[AddSprite](ParticleSystem.TextureSheetAnimationModule.AddSprite.html)| Add a
new Sprite.  
---|---  
[GetSprite](ParticleSystem.TextureSheetAnimationModule.GetSprite.html)| Get
the Sprite at the given index.  
[RemoveSprite](ParticleSystem.TextureSheetAnimationModule.RemoveSprite.html)|
Remove a Sprite from the given index in the array.  
[SetSprite](ParticleSystem.TextureSheetAnimationModule.SetSprite.html)| Set
the Sprite at the given index.  
  
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

