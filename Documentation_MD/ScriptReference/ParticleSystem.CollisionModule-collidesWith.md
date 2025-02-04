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
[ParticleSystem.CollisionModule](ParticleSystem.CollisionModule.html).collidesWith

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

public [LayerMask](LayerMask.html) collidesWith;

### Description

Control which Layers this Particle System collides with.

Additional resources: [LayerMask](LayerMask.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool layerToggle;
        private readonly int layer0 = 0;
        private readonly int layer1 = 1;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startColor = [Color.red](Color-red.html);  
      
            var shape = ps.shape;
            shape.shapeType = [ParticleSystemShapeType.Sphere](ParticleSystemShapeType.Sphere.html);  
      
            var collision = ps.collision;
            collision.enabled = true;
            collision.type = [ParticleSystemCollisionType.World](ParticleSystemCollisionType.World.html);
            collision.mode = [ParticleSystemCollisionMode.Collision3D](ParticleSystemCollisionMode.Collision3D.html);
            collision.bounce = 0.0f;  
      
            var collider1 = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            collider1.transform.parent = ps.transform;
            collider1.transform.localPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, 13.0f);
            collider1.transform.localScale = new [Vector3](Vector3.html)(20.0f, 20.0f, 20.0f);
            collider1.layer = layer0;  
      
            var collider2 = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            collider2.transform.parent = ps.transform;
            collider2.transform.localPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, -13.0f);
            collider2.transform.localScale = new [Vector3](Vector3.html)(20.0f, 20.0f, 20.0f);
            collider2.layer = layer1;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var collision = ps.collision;
            collision.collidesWith = layerToggle ? (1 << layer0) : (1 << layer1);
        }  
      
        void OnGUI()
        {
            layerToggle = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 40, 100, 30), layerToggle, "[Toggle](UIElements.Toggle.html) [Layer](Experimental.GraphView.GraphView.Layer.html)");
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

