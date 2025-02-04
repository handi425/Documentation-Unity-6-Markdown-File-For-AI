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
[ParticleSystem.ExternalForcesModule](ParticleSystem.ExternalForcesModule.html).SetInfluence

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

public void SetInfluence(int index,
[ParticleSystemForceField](ParticleSystemForceField.html) field);

### Parameters

index | Index to assign the Force Field.  
---|---  
field | Force Field that to assign.  
  
### Description

Assigns the Force Field at the given index in the influencers list.

When [influenceFilter](ParticleSystem.ExternalForcesModule-
influenceFilter.html) is set to
[ParticleSystemGameObjectFilter.List](ParticleSystemGameObjectFilter.List.html)
then only Force Fields in the influencers list affect the Particle System.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [ParticleSystem](ParticleSystem.html) system;
        public [ParticleSystemForceField](ParticleSystemForceField.html) field1;
        public [ParticleSystemForceField](ParticleSystemForceField.html) field2;  
      
        [ParticleSystem.ExternalForcesModule](ParticleSystem.ExternalForcesModule.html) m_ExternalForcesModule;  
      
        void Start()
        {
            if (system == null)
            {
                [Debug.LogError](Debug.LogError.html)("Please assign a [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html) to `system`.");
                enabled = false;
                return;
            }  
      
            if (field1 == null || field2 == null)
            {
                [Debug.LogError](Debug.LogError.html)("Please assign a [ParticleSystemForceField](ParticleSystemForceField.html) to `field1` and `field2`.");
                enabled = false;
                return;
            }  
      
            m_ExternalForcesModule = system.externalForces;
            m_ExternalForcesModule.enabled = true;
            m_ExternalForcesModule.influenceFilter = [ParticleSystemGameObjectFilter.List](ParticleSystemGameObjectFilter.List.html);
            m_ExternalForcesModule.AddInfluence(field1);
        }  
      
        void OnGUI()
        {
            [Debug.Assert](Debug.Assert.html)(m_ExternalForcesModule.influenceCount == 1);
            var currentForceField = m_ExternalForcesModule.GetInfluence(0);  
      
            [GUILayout.BeginHorizontal](GUILayout.BeginHorizontal.html)();
            [GUILayout.Label](GUILayout.Label.html)("Influence: " + currentForceField.name);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("[Toggle](UIElements.Toggle.html)"))
            {
                m_ExternalForcesModule.SetInfluence(0, currentForceField == field1 ? field2 : field1);
            }  
      
            [GUILayout.EndHorizontal](GUILayout.EndHorizontal.html)();
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

