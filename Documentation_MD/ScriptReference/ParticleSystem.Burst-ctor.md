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

# ParticleSystem.Burst Constructor

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

public ParticleSystem.Burst(float _time, short _count);

## Declaration

public ParticleSystem.Burst(float _time, short _minCount, short _maxCount);

## Declaration

public ParticleSystem.Burst(float _time, short _minCount, short _maxCount, int
_cycleCount, float _repeatInterval);

## Declaration

public ParticleSystem.Burst(float _time,
[ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html) _count);

## Declaration

public ParticleSystem.Burst(float _time,
[ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html) _count, int
_cycleCount, float _repeatInterval);

### Parameters

_time | Time to emit the burst.  
---|---  
_minCount | Minimum number of particles to emit.  
_maxCount | Maximum number of particles to emit.  
_count | Number of particles to emit.  
_cycleCount | Specifies how many times the system should play the burst. Set this to 0 to make it play indefinitely.  
_repeatInterval | How often to repeat the burst, in seconds.  
  
### Description

Construct a new Burst with a time and count.

Additional resources: ParticleSystem.emissionModule.SetBursts,
ParticleSystem.emissionModule.GetBursts.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Create a looping [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html).
    // At 0, 1 and 2 secs the number of particles in each loop
    // are changed from 10, to 50, then to 100.
    // The loops repeat after 3 seconds.  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Material](Material.html) part;  
      
        void Start()
        {
            // create a red ground plane
            [GameObject](GameObject.html) ground = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Quad](PrimitiveType.Quad.html));
            ground.transform.rotation = [Quaternion.Euler](Quaternion.Euler.html)(90, 0, 0);
            ground.transform.localScale = new [Vector3](Vector3.html)(10, 10, 10);
            ground.GetComponent<[Renderer](Renderer.html)>().material.color = [Color.red](Color-red.html);  
      
            // rotate the [GameObject](GameObject.html) so particles rise up in the y-axis
            gameObject.transform.rotation = [Quaternion.Euler](Quaternion.Euler.html)(-90, 0, 0);
            gameObject.AddComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            // create the [ParticleSystem](ParticleSystem.html)
            [ParticleSystem](ParticleSystem.html) ps;
            ps = gameObject.GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            ps.Stop();  
      
            // set the [MainModule](ParticleSystem.MainModule.html) default values
            var main = ps.main;
            main.startColor = [Color.yellow](Color-yellow.html);
            main.duration = 3;  
      
            // create a cone and change it into a cylinder
            var shape = ps.shape;
            shape.shapeType = [ParticleSystemShapeType.Cone](ParticleSystemShapeType.Cone.html);
            shape.angle = 0.0f;
            shape.radius = 2.0f;
            shape.radiusThickness = 0.0f;  
      
            // use the passed in material
            gameObject.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>().material = part;  
      
            // set up the emission to generate particles
            var em = ps.emission;
            em.enabled = true;
            em.rateOverTime = 0;  
      
            em.SetBursts(
                new [ParticleSystem.Burst](ParticleSystem.Burst.html)[]
                {
                    new [ParticleSystem.Burst](ParticleSystem.Burst.html)(0.0f, 10),
                    new [ParticleSystem.Burst](ParticleSystem.Burst.html)(1.0f, 50),
                    new [ParticleSystem.Burst](ParticleSystem.Burst.html)(2.0f, 100)
                });  
      
            ps.Play();
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

