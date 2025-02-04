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

# MenuCommand

class in UnityEditor

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

Used to extract the context for a [MenuItem](MenuItem.html).

[MenuCommand](MenuCommand.html) objects are passed to custom menu item
functions defined using the [MenuItem](MenuItem.html) attribute.  
  
**Note:** The menu is added to the object and is accessible by right-clicking
in the inspector. The script code requires the CONTEXT option.

    
    
    // Add context menu named "Do Something" to context menu
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Something : [EditorWindow](EditorWindow.html)
    {
        // Add menu item
        [[MenuItem](MenuItem.html)("CONTEXT/[Rigidbody](Rigidbody.html)/Do Something")]
        static void DoSomething([MenuCommand](MenuCommand.html) command)
        {
            [Rigidbody](Rigidbody.html) body = ([Rigidbody](Rigidbody.html))command.context;
            body.mass = 5;
            [Debug.Log](Debug.Log.html)("Changed [Rigidbody](Rigidbody.html)'s Mass to " + body.mass + " from Context [Menu](Menu.html)...");
        }
    }
    

Additional resources: [MenuItem](MenuItem.html).

### Properties

[context](MenuCommand-context.html)| Context is the object that is the target
of a menu command.  
---|---  
[userData](MenuCommand-userData.html)| An integer for passing custom
information to a menu item.  
  
### Constructors

[MenuCommand](MenuCommand-ctor.html)| Creates a new MenuCommand object.  
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

