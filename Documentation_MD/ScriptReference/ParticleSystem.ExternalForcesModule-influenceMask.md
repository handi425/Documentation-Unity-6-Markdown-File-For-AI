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
[ParticleSystem.ExternalForcesModule](ParticleSystem.ExternalForcesModule.html).influenceMask

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

public [LayerMask](LayerMask.html) influenceMask;

### Description

Particle System Force Field Components with a matching Layer affect this
Particle System.

Additional resources: [LayerMask](LayerMask.html).

    
    
    using UnityEngine;  
      
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
            shape.enabled = false;  
      
            var externalForces = ps.externalForces;
            externalForces.enabled = true;  
      
            var forceField1 = new [GameObject](GameObject.html)("Force Field 1", typeof([ParticleSystemForceField](ParticleSystemForceField.html))).GetComponent<[ParticleSystemForceField](ParticleSystemForceField.html)>();
            forceField1.transform.parent = ps.transform;
            forceField1.transform.localPosition = new [Vector3](Vector3.html)(-3.0f, 0.0f, 3.0f);
            forceField1.transform.localRotation = [Quaternion.Euler](Quaternion.Euler.html)(0.0f, 0.0f, 180.0f);
            forceField1.transform.localScale = new [Vector3](Vector3.html)(5.0f, 5.0f, 5.0f);
            forceField1.gameObject.layer = layer0;  
      
            forceField1.gravity = 0.04f;
            forceField1.rotationSpeed = 2.0f;
            forceField1.rotationAttraction = 0.02f;  
      
            var forceField2 = new [GameObject](GameObject.html)("Force Field 2", typeof([ParticleSystemForceField](ParticleSystemForceField.html))).GetComponent<[ParticleSystemForceField](ParticleSystemForceField.html)>();
            forceField2.transform.parent = ps.transform;
            forceField2.transform.localPosition = new [Vector3](Vector3.html)(3.0f, 0.0f, 3.0f);
            forceField2.transform.localRotation = [Quaternion.identity](Quaternion-identity.html);
            forceField2.transform.localScale = new [Vector3](Vector3.html)(5.0f, 5.0f, 5.0f);
            forceField2.gameObject.layer = layer1;  
      
            forceField2.gravity = 0.04f;
            forceField2.rotationSpeed = 2.0f;
            forceField2.rotationAttraction = 0.02f;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var externalForces = ps.externalForces;
            externalForces.influenceMask = layerToggle ? (1 << layer0) : (1 << layer1);
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

