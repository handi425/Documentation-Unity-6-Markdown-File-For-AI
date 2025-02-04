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

#  [AddComponentMenu](AddComponentMenu.html).componentOrder

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

public int componentOrder;

### Description

The order of the component in the component menu (lower values appear higher
in the menu).

**Note** : The order only affects the component item itself and doesn't
influence any submenus.  
  
Scripts are first sorted by their namespace. Scripts without a namespace are
positioned after those with a namespace.  
  
By default, menu items are assigned a position value of 20. The final
placement of the item is determined by adding the `componentOrder` value to
this default position. The order can be either positive or negative value.  
  
If your item has a priority of 11 or higher than the previous item, a
separator is automatically added before your item in the menu.  
  
The following example uses a `componentOrder` of `-1` to bring **MyScript2**
above **MyScript1** :

    
    
    using UnityEngine;  
      
    
    [[AddComponentMenu](AddComponentMenu.html)("My Scripts/My Script 1")]
    public class MyScript1 : [MonoBehaviour](MonoBehaviour.html)
    {
    }  
      
    [[AddComponentMenu](AddComponentMenu.html)("My Scripts/My Script 2", -1)]
    public class MyScript2 : [MonoBehaviour](MonoBehaviour.html)
    {
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

