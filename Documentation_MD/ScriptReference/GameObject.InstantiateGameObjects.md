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

#  [GameObject](GameObject.html).InstantiateGameObjects

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

## Declaration

public static void InstantiateGameObjects(int sourceInstanceID, int count,
NativeArray<int> newInstanceIDs, NativeArray<int> newTransformInstanceIDs,
[SceneManagement.Scene](SceneManagement.Scene.html) destinationScene);

### Parameters

sourceInstanceID | The instance ID of the GameObject to create additional instances of.  
---|---  
count | The number of instances of the GameObject to create.  
newInstanceIDs | Pre-allocated NativeArray to populate with the instance IDs of the new GameObjects. Must be the same size as `count`.  
newTransformInstanceIDs | Pre-allocated NativeArray to populate with the instance IDs of the Transforms of the new GameObjects. Must be the same size as `count`.  
destinationScene | The Scene to place the instantiated GameObjects into. If default, then the GameObjects will be added to the currently active Scene.  
  
### Description

Creates a specified number of instances of a GameObject identified by its
instance ID and populates NativeArrays with the instance IDs of the new
GameObjects and their Transform components.

Use `InstantiateGameObjects` to instantiate multiple GameObjects as a batch.
An instance ID can be resolved to an object using
[Resources.InstanceIDToObject](Resources.InstanceIDToObject.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Collections;
    using UnityEngine;  
      
    public class InstantiateInstanceID : [MonoBehaviour](MonoBehaviour.html)
    {
    public [GameObject](GameObject.html) prefab;
    public int count = 100;  
      
        int m_InstanceID;
        NativeArray<int> m_InstanceIds;
        NativeArray<int> m_TransformIds;
        
        void Start()
        {
            m_InstanceID = prefab.GetInstanceID();
            m_InstanceIds = new NativeArray<int>(count, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            m_TransformIds = new NativeArray<int>(count, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            
            [GameObject.InstantiateGameObjects](GameObject.InstantiateGameObjects.html)(m_InstanceID, count, m_InstanceIds,m_TransformIds );
        }  
      
        void OnDestroy()
        {
            m_InstanceIds.Dispose();
            m_TransformIds.Dispose();
        }
    }
    

Additional resources:
[GameObject.SetGameObjectsActive](GameObject.SetGameObjectsActive.html),
[Resources.InstanceIDToObject](Resources.InstanceIDToObject.html)

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

