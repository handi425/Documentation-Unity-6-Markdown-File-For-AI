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

#  [Sprite](Sprite.html).GetScriptableObjects

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

public uint GetScriptableObjects(ScriptableObject[] scriptableObjects);

### Parameters

scriptableObjects | The array of [ScriptableObject](ScriptableObject.html) to contain the ScriptableObjects referenced by the sprite.   
---|---  
  
### Returns

**uint** Returns the number of ScriptableObjects retrieved.

### Description

Retrieves an array of [ScriptableObject](ScriptableObject.html) referenced by
the sprite.

If the size of the arrays passed in as parameters are less than the number of
[ScriptableObject](ScriptableObject.html) referenced by the sprite, the arrays
will not be resized and the results will be limited.  
  
If the size of the arrays passed in as parameters are bigger than the number
of [ScriptableObject](ScriptableObject.html) referenced by the sprite, the
number of elements used in the array will be indicated by the return value of
the method.  
  
The following is an example usage of adding, getting and removing
ScriptableObjects reference to a sprite.

    
    
    using UnityEngine;  
      
    /*
     * Creates a custom [ScriptableObject](ScriptableObject.html) and attaches it
     * to a [Sprite](Sprite.html). The [ScriptableObject](ScriptableObject.html) is then removed after
     * the first [Update](PlayerLoop.Update.html) loop so that the messages are only printed once.
     */  
      
    // A custom [ScriptableObject](ScriptableObject.html) to hold any custom data.
    public class MyScriptableObject : [ScriptableObject](ScriptableObject.html)
    {
        public string myCustomData;
    }  
      
    public class [Sample](PackageManager.UI.Sample.html) : [MonoBehaviour](MonoBehaviour.html)
    {
        [Sprite](Sprite.html) m_Sprite;
        void Start()
        {
            var customData = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<MyScriptableObject>();
            customData.myCustomData = "My [Data](Unity.Android.Gradle.Manifest.Data.html)";
            var texture = [Texture2D.whiteTexture](Texture2D-whiteTexture.html);
            m_Sprite = [Sprite.Create](Sprite.Create.html)(texture, new [Rect](Rect.html)(0, 0, texture.width, texture.height), [Vector2.zero](Vector2-zero.html), texture.width);
            var spriteRenderer = gameObject.AddComponent<[SpriteRenderer](SpriteRenderer.html)>();
            m_Sprite.AddScriptableObject(customData);
            spriteRenderer.sprite = m_Sprite;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var scriptableObjectCount = m_Sprite.GetScriptableObjectsCount();
            if (scriptableObjectCount > 0)
            {
                var scriptableObjects = new [ScriptableObject](ScriptableObject.html)[scriptableObjectCount];
                var retrieveCount = m_Sprite.GetScriptableObjects(scriptableObjects);
                //This will print 1 since there is 1 [ScriptableObject](ScriptableObject.html) reference.
                print(retrieveCount);
                var myScriptableObject = scriptableObjects[0] as MyScriptableObject;
                // This will print "My [Data](Unity.Android.Gradle.Manifest.Data.html)"
                print(myScriptableObject.myCustomData);  
      
                // Removing the [ScriptableObject](ScriptableObject.html) reference so that the prints
                // above no longer executes.
                m_Sprite.RemoveScriptableObjectAt(scriptableObjectCount - 1);
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

