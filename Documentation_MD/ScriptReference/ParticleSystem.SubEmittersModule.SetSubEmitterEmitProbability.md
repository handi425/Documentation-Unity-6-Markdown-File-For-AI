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

#
[ParticleSystem.SubEmittersModule](ParticleSystem.SubEmittersModule.html).SetSubEmitterEmitProbability

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

public void SetSubEmitterEmitProbability(int index, float emitProbability);

### Parameters

index | The index of the sub-emitter you want to modify.  
---|---  
emitProbability | The probability value.  
  
### Description

Sets the probability that the sub-emitter emits particles.

Accepts a value from 0 to 1, where 0 is never and 1 is always.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // A simple particle material with no texture.
            var particleMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Surface"));  
      
            // Emit 1 particle per second.
            var particleSystemGameObject = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var particleSystemMain = particleSystemGameObject.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            var emitMain = particleSystemMain.emission;
            emitMain.rateOverTime = 1;
            particleSystemGameObject.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;  
      
            // Create a sub-emitter with a 10% chance to emit a red particle when "[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)" emits.
            var subEmitterGo = new [GameObject](GameObject.html)("Sub Emitter");
            subEmitterGo.transform.SetParent(particleSystemGameObject.transform);
            var subEmitter = subEmitterGo.AddComponent<[ParticleSystem](ParticleSystem.html)>();
            var emitSub = subEmitter.emission;
            emitSub.rateOverTime = 0;
            emitSub.burstCount = 1;
            emitSub.SetBurst(0, new [ParticleSystem.Burst](ParticleSystem.Burst.html)(0, 1));
            var mainModule = subEmitter.main;
            mainModule.startColor = [Color.red](Color-red.html);
            subEmitterGo.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = particleMaterial;  
      
            // Add the sub-emitter, and set the probability.
            var subEmittersModule = particleSystemMain.subEmitters;
            subEmittersModule.enabled = true;
            subEmittersModule.AddSubEmitter(subEmitter, [ParticleSystemSubEmitterType.Birth](ParticleSystemSubEmitterType.Birth.html), new [ParticleSystemSubEmitterProperties](ParticleSystemSubEmitterProperties.html)(), 0.1f);
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

