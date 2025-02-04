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

# OnOpenAssetAttribute

class in UnityEditor.Callbacks

/

Inherits from:[CallbackOrderAttribute](CallbackOrderAttribute.html)

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

Invokes a static callback method when the Unity Editor attempts to open an
asset.

Unity calls any static method decorated with `[OnOpenAssetAttribute]` when
attempting to open an asset, such as when double-clicking the asset in the
Editor. This offers the opportunity to implement custom asset opening logic or
to verify that an asset can open in the Unity Editor as opposed to an external
program.  
  
The attribute targets methods and accepts two optional positional parameters:

  * `callbackOrder`: The first parameter represents the index of the callback invocation order and must be of type `int`. This is useful if you have more than one [OnOpenAssetAttribute](Callbacks.OnOpenAssetAttribute.html) callbacks, and you would like them to be called in a certain order. Methods are called in ascending numerical order, starting from 0.
  * `attributeMode`: The second parameter is an `enum` value from [OnOpenAssetAttributeMode](Callbacks.OnOpenAssetAttributeMode.html) that indicates whether the decorated method is called in `Execute` or `Validate` mode. `Execute` mode is intended for callbacks that implement some custom asset-opening behavior. `Validate` mode is intended to check if the Editor can open the asset. If not specified the default mode is [OnOpenAssetAttributeMode.Execute](Callbacks.OnOpenAssetAttributeMode.Execute.html).

A method decorated with `[OnOpenAssetAttribute]` and in `Execute` mode must
have one of the following signatures:

  * `static bool OnOpenAsset(int instanceID)`
  * `static bool OnOpenAsset(int instanceID, int line)`
  * `static bool OnOpenAsset(int instanceID, int line, int column)`

**Note:** The callback method does not have to be named `OnOpenAsset` but its
signature must match one of those shown.  
  
A method decorated with `[OnOpenAssetAttribute]` and in `Validate` mode must
have the following signature:  
  
`static bool OnOpenAsset(int instanceID)`  
  
In
[OnOpenAssetAttributeMode.Validate](Callbacks.OnOpenAssetAttributeMode.Validate.html)
mode, the method does not open the asset but checks to see if the Editor can
open it. It returns `true` if the Editor can open the asset or `false`
otherwise. This is equivalent to the check
[AssetDatabase.CanOpenAssetInEditor](AssetDatabase.CanOpenAssetInEditor.html)
performs.  
  
Version control system integrations primarily use this validation function to
determine what files to check out. Native assets like GameObjects, Scenes, or
user-made assets return `true` because they are opened and edited in the
Editor. Assets like sound clips and textures return `false` because they're
opened and edited in an external program.  
  
See Also: [OnOpenAssetAttributeMode](Callbacks.OnOpenAssetAttributeMode.html),
[AssetDatabase.CanOpenAssetInEditor](AssetDatabase.CanOpenAssetInEditor.html)

    
    
    // Return true if you handled the opening of the asset or false if an external tool should open it.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;  
      
    public class MyAssetHandler : [ScriptableObject](ScriptableObject.html)
    {
        [[OnOpenAssetAttribute](Callbacks.OnOpenAssetAttribute.html)(1)]
        public static bool step1(int instanceID, int line)
        {
            string name = [EditorUtility.InstanceIDToObject](EditorUtility.InstanceIDToObject.html)(instanceID).name;
            [Debug.Log](Debug.Log.html)("Open [Asset](VersionControl.Asset.html) step: 1 (" + name + ")");
            return false; // we did not handle the open
        }  
      
        // step2 has an attribute with index 2, so will be called after step1
        [[OnOpenAssetAttribute](Callbacks.OnOpenAssetAttribute.html)(2)]
        public static bool step2(int instanceID, int line)
        {
            [Debug.Log](Debug.Log.html)("Open [Asset](VersionControl.Asset.html) step: 2 (" + instanceID + ")");
            return false; // we did not handle the open
        }  
      
        [OnOpenAsset([OnOpenAssetAttributeMode.Validate](Callbacks.OnOpenAssetAttributeMode.Validate.html))]
        public static bool WillOpenInUnity(int instanceID)
        {
            if ([AssetDatabase.GetMainAssetTypeAtPath](AssetDatabase.GetMainAssetTypeAtPath.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(instanceID)) == typeof(MyAssetHandler))
            {
                // We can open MyAssetHandler asset using MyAssetHandler opening method
                return true;
            }
            else  return false; // The passed instance doesn't belong to MyAssetHandler type asset so we won't be able to open it using opening method inside MyAssetHandler
        }
    }
    

### Inherited Members

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

