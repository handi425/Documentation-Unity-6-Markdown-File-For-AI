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

#  [GameObject](GameObject.html).FindGameObjectsWithTag

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

public static GameObject[] FindGameObjectsWithTag(string tag);

### Parameters

tag | The name of the tag to search for `GameObjects` by.  
---|---  
  
### Description

Retrieves an array of all active GameObjects tagged with the specified tag.
Returns an empty array if no GameObjects have the tag.

Tags must be declared in the tag manager before using them. A `UnityException`
will be thrown if the tag does not exist or if an empty string or `null` is
supplied as the `tag` parameter.

    
    
    // Instantiates respawnPrefab at the location
    // of all GameObjects tagged "Respawn".  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) respawnPrefab;
        public [GameObject](GameObject.html)[] respawns;
        void Start()
        {
            if (respawns == null)
                respawns = [GameObject.FindGameObjectsWithTag](GameObject.FindGameObjectsWithTag.html)("Respawn");  
      
            foreach ([GameObject](GameObject.html) respawn in respawns)
            {
                Instantiate(respawnPrefab, respawn.transform.position, respawn.transform.rotation);
            }
        }
    }
    

Another example:

    
    
    // Find the name of the closest enemy  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) FindClosestEnemy()
        {
            [GameObject](GameObject.html)[] gos;
            gos = [GameObject.FindGameObjectsWithTag](GameObject.FindGameObjectsWithTag.html)("Enemy");
            [GameObject](GameObject.html) closest = null;
            float distance = [Mathf.Infinity](Mathf.Infinity.html);
            [Vector3](Vector3.html) position = transform.position;
            foreach ([GameObject](GameObject.html) go in gos)
            {
                [Vector3](Vector3.html) diff = go.transform.position - position;
                float curDistance = diff.sqrMagnitude;
                if (curDistance < distance)
                {
                    closest = go;
                    distance = curDistance;
                }
            }
            return closest;
        }
    }
    

Another example, testing for empty array:

    
    
    using UnityEngine;  
      
    // Search for GameObjects with a tag that is not used  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [GameObject](GameObject.html)[] gameObjects;
            gameObjects = [GameObject.FindGameObjectsWithTag](GameObject.FindGameObjectsWithTag.html)("Enemy");  
      
            if (gameObjects.Length == 0)
            {
                [Debug.Log](Debug.Log.html)("No GameObjects are tagged with 'Enemy'");
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

