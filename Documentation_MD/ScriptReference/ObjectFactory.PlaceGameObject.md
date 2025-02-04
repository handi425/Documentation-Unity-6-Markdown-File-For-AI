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

#  [ObjectFactory](ObjectFactory.html).PlaceGameObject

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

public static void PlaceGameObject([GameObject](GameObject.html) go,
[GameObject](GameObject.html) parent);

### Parameters

go | The GameObject to be initialized.  
---|---  
parent | An optional GameObject to be set as the parent.  
  
### Description

Place the given GameObject in the Scene View using the same preferences as
built-in Unity GameObjects.

Use this method to create GameObjects centered in the Scene View or at world
origin, depending on user preference. This method also ensures that the
GameObject has a unique name, also as defined by preferences.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // Creates a new [GameObject](GameObject.html) with the same preferences that built-in GameObjects instantiate with.
    class CreateGameObjectExample
    {
        [[MenuItem](MenuItem.html)("[GameObject](GameObject.html)/3D Object/My Cube")]
        static void CreateCube([MenuCommand](MenuCommand.html) command)
        {
            var gameObject = [ObjectFactory.CreatePrimitive](ObjectFactory.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            [ObjectFactory.PlaceGameObject](ObjectFactory.PlaceGameObject.html)(gameObject, command.context as [GameObject](GameObject.html));
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

