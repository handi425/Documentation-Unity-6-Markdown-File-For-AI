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
[ParticleSystem.ExternalForcesModule](ParticleSystem.ExternalForcesModule.html).RemoveInfluence

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

public void RemoveInfluence(int index);

## Declaration

public void
RemoveInfluence([ParticleSystemForceField](ParticleSystemForceField.html)
field);

### Parameters

index | The index to remove the chosen Force Field from.  
---|---  
field | The Force Field to remove from the list.  
  
### Description

Removes the Force Field from the influencers list at the given index.

When [influenceFilter](ParticleSystem.ExternalForcesModule-
influenceFilter.html) is set to
[ParticleSystemGameObjectFilter.List](ParticleSystemGameObjectFilter.List.html)
then only Force Fields in the influencers list affect the Particle System.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem.ExternalForcesModule](ParticleSystem.ExternalForcesModule.html) externalForcesModule;  
      
        void Start()
        {
            // Create a default particle system
            var particleSystemGameObject = new [GameObject](GameObject.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)");
            var system = particleSystemGameObject.AddComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            // Create a force field to influence the particle system
            var forceFieldGameObject = new [GameObject](GameObject.html)("Force Field");
            var forceField = forceFieldGameObject.AddComponent<[ParticleSystemForceField](ParticleSystemForceField.html)>();
            forceField.endRange = 5;
            forceFieldGameObject.transform.position = new [Vector3](Vector3.html)(0, 0, 10);  
      
            // Add the force to the particle systems external forces influencers.
            externalForcesModule = system.externalForces;
            externalForcesModule.enabled = true;
            externalForcesModule.influenceFilter = [ParticleSystemGameObjectFilter.List](ParticleSystemGameObjectFilter.List.html);
            externalForcesModule.AddInfluence(forceField);
        }  
      
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("[Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html) Influencers:");
            for (int i = 0; i < externalForcesModule.influenceCount; ++i)
            {
                var influence = externalForcesModule.GetInfluence(i);  
      
                [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
                [GUILayout.Label](GUILayout.Label.html)(i + ": " + influence.name);
                if ([GUILayout.Button](GUILayout.Button.html)("Remove"))
                {
                    externalForcesModule.RemoveInfluence(i);
                    --i;
                }
                [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
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

