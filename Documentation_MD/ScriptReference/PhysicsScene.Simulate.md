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

#  [PhysicsScene](PhysicsScene.html).Simulate

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

[ ]()

## Declaration

public void Simulate(float step);

### Parameters

step | The time to advance physics by.  
---|---  
  
### Returns

**void** Whether the simulation was run or not. Running the simulation during
physics callbacks will always fail.

### Description

Simulate physics associated with this [PhysicsScene](PhysicsScene.html).

Calling this method causes the physics to be simulated over the specified
`step` time. Only the physics associated with this
[PhysicsScene](PhysicsScene.html) will be simulated. If this
[PhysicsScene](PhysicsScene.html) is not the default physics Scene (see
[Physics.defaultPhysicsScene](Physics-defaultPhysicsScene.html)) then it is
associated with a specific [Scene](SceneManagement.Scene.html) and as such,
only components added to that [Scene](SceneManagement.Scene.html) are affected
when running the simulation.  
  
If you pass framerate-dependent step values (such as [Time.deltaTime](Time-
deltaTime.html)) to the physics engine, your simulation will be less
deterministic because of the unpredictable fluctuations in framerate that can
arise. To achieve more deterministic physics results, you should pass a fixed
step value to [PhysicsScene.Simulate](PhysicsScene.Simulate.html) every time
you call it.  
  
You can call [PhysicsScene.Simulate](PhysicsScene.Simulate.html) in the Editor
outside of play mode however caution is advised as this will cause the
simulation to move GameObject that have a [Rigidbody](Rigidbody.html)
component attached. When simulating in the Editor outside of play mode, a full
simulation occurs for all physics components including
[Rigidbody](Rigidbody.html), [Collider](Collider.html) and [Joint](Joint.html)
including the generation of contacts however contacts are not reported via the
standard script callbacks. This is a safety measure to prevent allowing
callbacks to delete objects in the Scene which would not be an undoable
operation. Here is an example of a basic simulation that implements what's
being done in the automatic simulation mode.

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class MultiScenePhysics : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Scene](SceneManagement.Scene.html) extraScene;  
      
        public void Start()
        {
            // First create an extra scene with local physics
            extraScene = [SceneManager.CreateScene](SceneManagement.SceneManager.CreateScene.html)("[Scene](SceneManagement.Scene.html)", new [CreateSceneParameters](SceneManagement.CreateSceneParameters.html)([LocalPhysicsMode.Physics3D](SceneManagement.LocalPhysicsMode.Physics3D.html)));  
      
            // Mark the scene active, so that all the new GameObjects end up in the newly created scene
            [SceneManager.SetActiveScene](SceneManagement.SceneManager.SetActiveScene.html)(extraScene);  
      
            PopulateExtraSceneWithObjects();
        }  
      
        public void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            // All of the non-default physics scenes need to be simulated manually
            var physicsScene = extraScene.GetPhysicsScene();
            physicsScene.Simulate([Time.fixedDeltaTime](Time-fixedDeltaTime.html));
        }  
      
        public void PopulateExtraSceneWithObjects()
        {
            // Create GameObjects for physics simulation
            var sphere = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            sphere.AddComponent<[Rigidbody](Rigidbody.html)>();
            sphere.transform.position = [Vector3.up](Vector3-up.html) * 4;
        }
    }
    

Additional resources: [Physics.Simulate](Physics.Simulate.html).

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

