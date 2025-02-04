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

# LazyLoadReference<T0>

struct in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Serializable lazy reference to a UnityEngine.Object contained in an asset
file.

Allows an asset to reference another asset but delays loading the referenced
asset until it is used, instead of loading it when the referencing object is
deserialized.  
  
**Typical use cases** :  
\- For importer settings that need to reference assets but reading the
settings from disk cannot load the referenced assets because they may not be
imported and are not yet accessible.  
\- For reducing the time it takes to open a scene by loading only the assets
needed for the initial set up, or display, in Edit Mode.  
  
**Notes:**

  * A lazy reference has a slight performance overhead compared to a direct reference.
  * In a standalone player, all assets are loaded when the player is loaded, or when asset bundles are loaded.

    
    
    using UnityEditor.AssetImporters;
    using UnityEngine;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "foo")]
    public class FooImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public LazyLoadReference<[Material](Material.html)> m_DefaultMaterial;  
      
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            // At this point, 'm_DefaultMaterial' may refer to a material that has yet to be loaded into memory  
      
            [Material](Material.html) mat;
            if (!m_DefaultMaterial.isSet) // 'isSet' Does not load the referenced material even if not in memory.
            {
                mat = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Transparent/Diffuse"));
                ctx.AddObjectToAsset("mat", mat);
            }
            else
            {
                mat = m_DefaultMaterial.asset; // Will load referenced material if it is not already in memory.
            }  
      
            var obj = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            obj.transform.GetComponent<[MeshRenderer](MeshRenderer.html)>().material = mat;  
      
            ctx.AddObjectToAsset("main", obj);
            ctx.SetMainObject(obj);
        }
    }
    

### Properties

[asset](LazyLoadReference_1-asset.html)| Accessor to the referenced asset.  
---|---  
[instanceID](LazyLoadReference_1-instanceID.html)| Returns the instance id to
the referenced asset.  
[isBroken](LazyLoadReference_1-isBroken.html)| Convenience property that
checks whether the reference is broken: refers to an object that is either not
available or not loadable.  
[isSet](LazyLoadReference_1-isSet.html)| Determines if an asset is being
targeted, regardless of whether the asset is available for loading.  
  
### Constructors

[LazyLoadReference_1](LazyLoadReference_1-ctor.html)| Construct a new
LazyLoadReference.  
---|---  
  
### Operators

[LazyLoadReference<T>](LazyLoadReference_1-operator_T.html)| Implicit
conversion from asset reference to LazyLoadReference.  
---|---  
[LazyLoadReference<T>](LazyLoadReference_1-operator_int.html)| Implicit
conversion from instance ID to LazyLoadReference.  
  
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

