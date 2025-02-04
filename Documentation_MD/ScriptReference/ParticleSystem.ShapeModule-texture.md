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

#  [ParticleSystem.ShapeModule](ParticleSystem.ShapeModule.html).texture

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

public [Texture2D](Texture2D.html) texture;

### Description

Specifies a Texture to tint the particle's start colors.

To tint the particles' start color, the Shape module reads pixels from this
Texture on the CPU. This means you must enable the read/write option in the
assigned Texture's Import Settings.  
  
To tint particles, the Shape module first stretches the Texture over the shape
you specify. Then, when the system emits a particle from a point on the shape,
the Shape module uses the color of the Texture at that location as the
particle color.  
  
To see how the Texture stretches over the shape, select the Particle System in
the Hierarchy view and expand the Shape module. The Scene View visualization
of the shape includes the Texture preview.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float alphaThreshold = 0.0f;
        public bool colorAffectsParticles = true;
        public bool alphaAffectsParticles = true;
        public bool bilinearFiltering = false;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startSpeed = 0.0f;
            main.startSize = 0.5f;
            main.startLifetime = 1.0f;  
      
            var emission = ps.emission;
            emission.rateOverTime = 500.0f;  
      
            var shape = ps.shape;
            shape.shapeType = [ParticleSystemShapeType.Circle](ParticleSystemShapeType.Circle.html);
            shape.radius = 6.0f;
            shape.texture = AssetDatabase.GetBuiltinExtraResource<[Texture2D](Texture2D.html)>("Default-Particle.psd");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var shape = ps.shape;
            shape.textureClipThreshold = alphaThreshold;
            shape.textureColorAffectsParticles = colorAffectsParticles;
            shape.textureAlphaAffectsParticles = alphaAffectsParticles;
            shape.textureBilinearFiltering = bilinearFiltering;
        }  
      
        void OnGUI()
        {
            float y = 120.0f;
            float spacing = 40.0f;  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, y, 140, 30), "Alpha Threshold");
            alphaThreshold = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(165, y + 5, 100, 30), alphaThreshold, 0.0f, 1.0f);
            y += spacing;  
      
            colorAffectsParticles = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, y + 5, 200, 30), colorAffectsParticles, "[Color](Color.html) Affects Particles");
            y += spacing;  
      
            alphaAffectsParticles = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, y + 5, 200, 30), alphaAffectsParticles, "Alpha Affects Particles");
            y += spacing;  
      
            bilinearFiltering = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, y + 5, 200, 30), bilinearFiltering, "Bilinear Filtering");
            y += spacing;
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

