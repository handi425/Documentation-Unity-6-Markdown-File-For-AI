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

# ExposedReference<T0>

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Creates a type whos value is resolvable at runtime.

ExposedReference is a generic type that can be used to create references to
Scene objects and resolve their actual values at runtime and by using a
context object. This can be used by assets, such as a
[ScriptableObject](ScriptableObject.html) or
[PlayableAsset](Playables.PlayableAsset.html) to create references to Scene
objects.  
  
The example below shows how a [PlayableAsset](Playables.PlayableAsset.html)
can use exposed references to create references to a Scene GameObject. This is
an example that uses Timeline, so you may want to [set up your GameObject in
Timeline](https://docs.unity3d.com/Packages/com.unity.timeline@latest/index.html?subfolder=/manual/wf-
create-instance.html) and [make an animation with your
GameObject](https://docs.unity3d.com/Packages/com.unity.timeline@latest/index.html?subfolder=/manual/wf-
record-anim.html).

    
    
    //Put both of these scripts in your Project, then go to your Timeline, click the **Add** dropdown and choose **Playable Track**. Place this script on your Timeline as a [Playable](Playables.Playable.html) Track
    //Click on the track and choose a [GameObject](GameObject.html) from your [Scene](SceneManagement.Scene.html) in the "My [Scene](SceneManagement.Scene.html) Object" field. Also set the velocity.  
      
    using UnityEngine;
    using UnityEngine.Playables;  
      
    [System.Serializable]
    public class ExposedReferenceExample : [PlayableAsset](Playables.PlayableAsset.html)
    {
        //This allows you to use GameObjects in your [Scene](SceneManagement.Scene.html)
        public ExposedReference<[GameObject](GameObject.html)> m_MySceneObject;
        //This variable allows you to decide the velocity of your [GameObject](GameObject.html)
        public [Vector3](Vector3.html) m_SceneObjectVelocity;  
      
        public  override [Playable](Playables.Playable.html) CreatePlayable([PlayableGraph](Playables.PlayableGraph.html) graph , [GameObject](GameObject.html) myGameObject)
        {
            //Get access to the [Playable](Playables.Playable.html) [Behaviour](Behaviour.html) script
            TestExample playableBehaviour = new TestExample();
            //Resolve the exposed reference on the [Scene](SceneManagement.Scene.html) [GameObject](GameObject.html) by returning the table used by the graph
            playableBehaviour.m_MySceneObject = m_MySceneObject.Resolve(graph.GetResolver());  
      
            //Make the [PlayableBehaviour](Playables.PlayableBehaviour.html) velocity variable the same as the variable you set
            playableBehaviour.m_SceneObjectVelocity = m_SceneObjectVelocity;  
      
            //Create a custom playable from this script using the Player [Behaviour](Behaviour.html) script
            return ScriptPlayable<TestExample>.Create(graph, playableBehaviour);
        }
    }
    

Place this next script in your Project in the same folder as the above script.
This script changes the behaviour of the timeline by moving the Scene
GameObject while the Playable Track is playing.

    
    
    using  UnityEngine;
    using  UnityEngine.Playables;  
      
    public  class TestExample : [PlayableBehaviour](Playables.PlayableBehaviour.html)
    {
        public [GameObject](GameObject.html) m_MySceneObject;
        public [Vector3](Vector3.html) m_SceneObjectVelocity;  
      
        public override void PrepareFrame([Playable](Playables.Playable.html) playable, [FrameData](Playables.FrameData.html) frameData)
        {
            //If the [Scene](SceneManagement.Scene.html) [GameObject](GameObject.html) exists, move it continuously until the [Playable](Playables.Playable.html) pauses
            if (m_MySceneObject != null)
                //Move the [GameObject](GameObject.html) using the velocity you set in your [Playable](Playables.Playable.html) Track's inspector
                m_MySceneObject.transform.Translate(m_SceneObjectVelocity);
        }
    }
    

### Properties

[defaultValue](ExposedReference_1-defaultValue.html)| The default value, in
case the value cannot be resolved.  
---|---  
[exposedName](ExposedReference_1-exposedName.html)| The name of the
ExposedReference.  
  
### Public Methods

[Resolve](ExposedReference_1.Resolve.html)| Gets the value of the reference by
resolving it given the ExposedPropertyResolver context object.  
---|---  
  
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

