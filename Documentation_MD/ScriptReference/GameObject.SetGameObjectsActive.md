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

#  [GameObject](GameObject.html).SetGameObjectsActive

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

public static void SetGameObjectsActive(NativeArray<int> instanceIDs, bool
active);

## Declaration

public static void SetGameObjectsActive(ReadOnlySpan<int> instanceIDs, bool
active);

### Parameters

instanceIDs | Instance IDs of GameObjects to activate or deactive.  
---|---  
active | The active state to set, where `true` sets the GameObjects to active and `false` sets them to inactive.  
  
### Description

Activates or deactivates multiple GameObjects identified by instance ID.

Use `SetGameObjectsActive` to activate or deactivate multiple GameObjects as a
batch.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.InputSystem;  
      
    //Add this script to a [GameObject](GameObject.html). This example requires the [Input](Input.html) [System](Rendering.VirtualTexturing.System.html) package.  
      
    public class DeactivateGOComponent : [MonoBehaviour](MonoBehaviour.html)
    {
    public [GameObject](GameObject.html) prefab;
    public int count = 100;  
      
        NativeArray<int> m_SpawnedInstanceIDsNative;
        int[] m_SpawnedInstanceIDs;
        
        bool m_SetActive = false;
        bool m_UseSlowMethod = false;
        
        void Start()
        {
            m_SpawnedInstanceIDs = new int[count];
            
            //Spawn some prefabs 
            for (int i = 0; i < count; i++)
            {
                //Save their instanceID
                m_SpawnedInstanceIDs[i] = Instantiate(prefab).GetInstanceID();
            }
            
            //Create native array with instanceIDs
            m_SpawnedInstanceIDsNative = new NativeArray<int>(m_SpawnedInstanceIDs, [Allocator.Persistent](Unity.Collections.Allocator.Persistent.html));
            
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (Keyboard.current[Key.A].wasPressedThisFrame)
            {
                if (m_UseSlowMethod)
                {
                    SetActiveSlow(m_SetActive);
                }
                else
                {
                    SetActiveFast(m_SpawnedInstanceIDsNative, m_SetActive);
                    
                }
                m_SetActive = !m_SetActive; 
            }
        }
        
        void SetActiveSlow(bool setActive)
        {
            foreach(int id in m_SpawnedInstanceIDs)
            {
                (([GameObject](GameObject.html))[Resources.InstanceIDToObject](Resources.InstanceIDToObject.html)(id)).SetActive(setActive);
            }
        }
        
        static void SetActiveFast(NativeArray<int> ids, bool setActive)
        {
            [GameObject.SetGameObjectsActive](GameObject.SetGameObjectsActive.html)(ids, setActive);
        }  
      
        void OnDestroy()
        {
            m_SpawnedInstanceIDsNative.Dispose();
        }
    }
    

Additional resources: [GameObject.SetActive](GameObject.SetActive.html),
[GameObject.InstantiateGameObjects](GameObject.InstantiateGameObjects.html).

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

