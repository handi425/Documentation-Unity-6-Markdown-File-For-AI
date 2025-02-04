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

#  [ObjectFactory](ObjectFactory.html).AddComponent

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

public static [Component](Component.html)
AddComponent([GameObject](GameObject.html) gameObject, Type type);

## Declaration

public static T AddComponent([GameObject](GameObject.html) gameObject);

### Parameters

gameObject | The GameObject to add the new component to.  
---|---  
type | The type of component to create and add to the GameObject.  
  
### Returns

**Component** Returns the component that was created and added to the
GameObject.

### Description

Creates a new component and adds it to the specified GameObject.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CreateComponentExample
    {
        [[MenuItem](MenuItem.html)("ObjectFactoryExample/Add [Camera](Camera.html) to [Selection](Selection.html)")]
        public void AddDefaultComponentEditor()
        {
            if ([Selection.activeGameObject](Selection-activeGameObject.html) != null)
            {
                [Camera](Camera.html) camera = [ObjectFactory.AddComponent](ObjectFactory.AddComponent.html)<[Camera](Camera.html)>([Selection.activeGameObject](Selection-activeGameObject.html));
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

