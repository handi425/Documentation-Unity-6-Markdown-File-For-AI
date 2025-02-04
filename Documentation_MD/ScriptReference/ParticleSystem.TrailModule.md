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

# TrailModule

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

Script interface for the TrailsModule.

This module adds trails to your particles. For example, you can make the
trails stay in the wake of particles as they move, or make them connect each
particle in the system together.  
  
Additional resources: [ParticleSystem](ParticleSystem.html),
[ParticleSystem.trails](ParticleSystem-trails.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [ParticleSystem](ParticleSystem.html) ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var trails = ps.trails;
            trails.enabled = true;
            trails.ratio = 0.5f;
        }
    }
    

### Properties

[attachRibbonsToTransform](ParticleSystem.TrailModule-
attachRibbonsToTransform.html)| Adds an extra position to each ribbon,
connecting it to the location of the Transform Component.  
---|---  
[colorOverLifetime](ParticleSystem.TrailModule-colorOverLifetime.html)| The
gradient that controls the trail colors during the lifetime of the attached
particle.  
[colorOverTrail](ParticleSystem.TrailModule-colorOverTrail.html)| The gradient
that controls the trail colors over the length of the trail.  
[dieWithParticles](ParticleSystem.TrailModule-dieWithParticles.html)|
Specifies whether trails disappear immediately when their owning particle
dies. When false, each trail persists until all its points have naturally
expired, based on its lifetime.  
[enabled](ParticleSystem.TrailModule-enabled.html)| Specifies whether the
TrailModule is enabled or disabled.  
[generateLightingData](ParticleSystem.TrailModule-generateLightingData.html)|
Configures the trails to generate Normals and Tangents. With this data, Scene
lighting can affect the trails via Normal Maps and the Unity Standard Shader,
or your own custom-built Shaders.  
[inheritParticleColor](ParticleSystem.TrailModule-inheritParticleColor.html)|
Toggle whether the trail inherits the particle color as its starting color.  
[lifetime](ParticleSystem.TrailModule-lifetime.html)| The curve describing the
trail lifetime, throughout the lifetime of the particle.  
[lifetimeMultiplier](ParticleSystem.TrailModule-lifetimeMultiplier.html)| A
multiplier for ParticleSystem.TrailModule.lifetime.  
[minVertexDistance](ParticleSystem.TrailModule-minVertexDistance.html)| Set
the minimum distance each trail can travel before the system adds a new vertex
to it.  
[mode](ParticleSystem.TrailModule-mode.html)| Choose how the system generates
the particle trails.  
[ratio](ParticleSystem.TrailModule-ratio.html)| Choose what proportion of
particles receive a trail.  
[ribbonCount](ParticleSystem.TrailModule-ribbonCount.html)| Select how many
lines to create through the Particle System.  
[shadowBias](ParticleSystem.TrailModule-shadowBias.html)| Apply a shadow bias
to prevent self-shadowing artifacts. The specified value is the proportion of
the trail width at each segment.  
[sizeAffectsLifetime](ParticleSystem.TrailModule-sizeAffectsLifetime.html)|
Set whether the particle size acts as a multiplier on top of the trail
lifetime.  
[sizeAffectsWidth](ParticleSystem.TrailModule-sizeAffectsWidth.html)| Set
whether the particle size acts as a multiplier on top of the trail width.  
[splitSubEmitterRibbons](ParticleSystem.TrailModule-
splitSubEmitterRibbons.html)| Specifies whether, if you use this system as a
sub-emitter, ribbons connect particles from each parent particle
independently.  
[textureMode](ParticleSystem.TrailModule-textureMode.html)| Choose whether the
U coordinate of the trail Texture is tiled or stretched.  
[textureScale](ParticleSystem.TrailModule-textureScale.html)| A multiplier for
the UV coordinates of the trail texture.  
[widthOverTrail](ParticleSystem.TrailModule-widthOverTrail.html)| The curve
describing the width of each trail point.  
[widthOverTrailMultiplier](ParticleSystem.TrailModule-
widthOverTrailMultiplier.html)| A multiplier for
ParticleSystem.TrailModule.widthOverTrail.  
[worldSpace](ParticleSystem.TrailModule-worldSpace.html)| Drop new trail
points in world space, regardless of Particle System Simulation Space.  
  
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

