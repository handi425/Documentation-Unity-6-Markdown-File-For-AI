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

#  [ArticulationBody](ArticulationBody.html).PublishTransform

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

[Switch to Manual](../Manual/class-ArticulationBody.html "Go to
ArticulationBody Component in the Manual")

## Declaration

public void PublishTransform();

### Description

Reads the position and rotation of the Articulation Body from the physics
system and applies it to the corresponding [Transform](Transform.html)
component.

Note: This method doesn't update the child Transforms. It should be called
from the topmost Transform, down the hierarchy.

    
    
    using System.Linq;
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private [PhysicsScene](PhysicsScene.html) m_SomeScene;
        private [ArticulationBody](ArticulationBody.html) m_RootArticulation;  
      
        public void SimulateTrajectory(float totalTime)
        {
            m_SomeScene.RunSimulationStages(0f, [SimulationStage.PrepareSimulation](SimulationStage.PrepareSimulation.html));  
      
            for (int i = 0; i < totalTime / [Time.fixedDeltaTime](Time-fixedDeltaTime.html); i++)
                m_SomeScene.RunSimulationStages([Time.fixedDeltaTime](Time-fixedDeltaTime.html), [SimulationStage.RunSimulation](SimulationStage.RunSimulation.html));  
      
            // Transforms of the [ArticulationBody](ArticulationBody.html) tree are still like they were at the start of the method  
      
            var links = m_RootArticulation.gameObject.GetComponentsInChildren<[ArticulationBody](ArticulationBody.html)>().ToList();
            links.Sort((a0, a1) => a0.index.CompareTo(a1.index));
            foreach (var ab in links)
                ab.PublishTransform();  
      
            // Transforms of the [ArticulationBody](ArticulationBody.html) tree are now up to date and can be accessed to see where the bodies ended up after simulating for "totalTime" seconds
        }  
      
        // Teleports the root body of the Articulation and applies the resulting position and rotation to the [Transform](Transform.html) component
        public void TeleportAndUpdate([Vector3](Vector3.html) position, [Quaternion](Quaternion.html) rotation)
        {
            m_RootArticulation.TeleportRoot(position, rotation);
            m_RootArticulation.PublishTransform();
        }
    }
    

Simulate a [PhysicsScene](PhysicsScene.html) with an
[ArticulationBody](ArticulationBody.html) and use
[PublishTransform](ArticulationBody.PublishTransform.html) to read the
information from the physics system to the [Transform](Transform.html)
component.

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

