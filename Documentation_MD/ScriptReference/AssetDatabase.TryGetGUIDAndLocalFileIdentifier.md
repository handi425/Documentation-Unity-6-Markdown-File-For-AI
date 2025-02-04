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

#  [AssetDatabase](AssetDatabase.html).TryGetGUIDAndLocalFileIdentifier

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

public static bool TryGetGUIDAndLocalFileIdentifier([Object](Object.html) obj,
out string guid, out long localId);

## Declaration

public static bool TryGetGUIDAndLocalFileIdentifier(int instanceID, out string
guid, out long localId);

## Declaration

public static bool TryGetGUIDAndLocalFileIdentifier(LazyLoadReference<T>
assetRef, out string guid, out long localId);

### Parameters

instanceID | InstanceID of the object to retrieve information for.  
---|---  
obj | The object to retrieve GUID and File Id for.  
assetRef | The asset reference to retrieve GUID and File Id for.  
guid | The GUID of an asset.  
localId | The local file identifier of this asset.  
  
### Returns

**bool** True if the guid and file id were successfully found, false if not.

### Description

Get the GUID and local file id from an object instance id.

**Warning:** Avoid the obsolete versions of this function, which use `int` for
the `localId` parameter instead of `long`. Local Ids can be longer than 32
bits in some cases, such as for Prefabs. When Unity serializes an asset
reference it points to two things: the GUID and file ID. GUID is a unique
hash, and file ID is a value relative to the asset. Both of these values are
used when a serialized asset references another asset.  
  
If working with a text serialized project (see [Editor
Settings](../Manual/class-EditorManager.html)) it is possible to manually
modify this information. A common use is moving C# script files from a project
to a DLL while keeping any GameObjects using these scripts intact. As an
example, suppose your project contains a C# MonoBehaviour, a Scene, and a
GameObject with this script attached. When serialized the Unity Scene file
will contain something that looks like this (reduced to the relevant parts):

    
    
    /* example .unity [Scene](SceneManagement.Scene.html) contents:  
      
    --- !u!1 &65078845
    [GameObject](GameObject.html):
      m_Component:
      -component: {fileID : 65078850}
    --- !u!114 &65078850
    [MonoBehaviour](MonoBehaviour.html):
      m_Script: {fileID : 11500000, guid : 9cbd8cdf99d44b58972fbc7f6f38088f, type : 3}  
      
    */
    
    
    
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class ShowAssetIds
    {
        [[MenuItem](MenuItem.html)("Assets/Show [Asset](VersionControl.Asset.html) Ids")]
        static void MenuShowIds()
        {
            var stringBuilder = new StringBuilder();  
      
            foreach (var obj in [AssetDatabase.LoadAllAssetsAtPath](AssetDatabase.LoadAllAssetsAtPath.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)([Selection.activeObject](Selection-activeObject.html))))
            {
                string guid;
                long file;  
      
                if ([AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(obj, out guid, out file))
                {
                    stringBuilder.AppendFormat("[Asset](VersionControl.Asset.html): " + obj.name +
                        "\n  Instance ID: " + obj.GetInstanceID() +
                        "\n  GUID: " + guid +
                        "\n  [File](Windows.File.html) ID: " + file);
                }
            }  
      
            [Debug.Log](Debug.Log.html)(stringBuilder.ToString());
        }
    }
    

Additional resources: [GlobalObjectId](GlobalObjectId.html)

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

