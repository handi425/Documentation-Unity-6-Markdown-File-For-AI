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

# MaterialPropertyBlock

class in UnityEngine

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

A block of material values to apply.

MaterialPropertyBlock is used by
[Graphics.RenderMesh](Graphics.RenderMesh.html) and
[Renderer.SetPropertyBlock](Renderer.SetPropertyBlock.html). Use it in
situations where you want to draw multiple objects with the same material, but
slightly different properties. For example, if you want to slightly change the
color of each mesh drawn. Changing the render state is not supported.  
  
Unity's terrain engine uses MaterialPropertyBlock to draw trees; all of them
use the same material, but each tree has different color, scale & wind factor.  
  
The block passed to [Graphics.RenderMesh](Graphics.RenderMesh.html) or
[Renderer.SetPropertyBlock](Renderer.SetPropertyBlock.html) is copied, so the
most efficient way of using it is to create one block and reuse it for all
DrawMesh calls. Use [SetFloat](MaterialPropertyBlock.SetFloat.html),
[SetVector](MaterialPropertyBlock.SetVector.html),
[SetColor](MaterialPropertyBlock.SetColor.html),
[SetMatrix](MaterialPropertyBlock.SetMatrix.html),
[SetTexture](MaterialPropertyBlock.SetTexture.html),
[SetBuffer](MaterialPropertyBlock.SetBuffer.html) to add or replace values.  
  
Note that this is not compatible with [SRP
Batcher](../Manual/SRPBatcher.html). Using this in the Universal Render
Pipeline (URP), High Definition Render Pipeline (HDRP) or a custom render
pipeline based on the Scriptable Render Pipeline (SRP) will likely result in a
drop in performance.  
  
The following example creates 10 GameObjects with random colors using
`MaterialPropertyBlock`. To use the example, attach a prefab to the `myPrefab`
property.  
  
Additional resources: [Graphics.RenderMesh](Graphics.RenderMesh.html),
[Material](Material.html).

    
    
    using UnityEngine;  
      
    public class CreateTenGameObjects : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) myPrefab;  
      
        void Start()
        {
            // Loop through 10 GameObjects
            for (int i = 0; i < 10; i++)
            {
                // Instantiate a new [GameObject](GameObject.html) at a unique position
                [GameObject](GameObject.html) newObject = Instantiate(myPrefab, new [Vector3](Vector3.html)(i * 2f, 0, 0), [Quaternion.identity](Quaternion-identity.html));  
      
                // Create a new [MaterialPropertyBlock](MaterialPropertyBlock.html)
                [MaterialPropertyBlock](MaterialPropertyBlock.html) propertyBlock = new [MaterialPropertyBlock](MaterialPropertyBlock.html)();  
      
                // Set a random color in the [MaterialPropertyBlock](MaterialPropertyBlock.html)
                propertyBlock.SetColor("_Color", [Random.ColorHSV](Random.ColorHSV.html)());  
      
                // Apply the [MaterialPropertyBlock](MaterialPropertyBlock.html) to the [GameObject](GameObject.html)
                newObject.GetComponent<[MeshRenderer](MeshRenderer.html)>().SetPropertyBlock(propertyBlock);
            }
        }
    }
    

### Properties

[isEmpty](MaterialPropertyBlock-isEmpty.html)| Is the material property block
empty? (Read Only)  
---|---  
  
### Public Methods

[Clear](MaterialPropertyBlock.Clear.html)| Clear material property values.  
---|---  
[CopyProbeOcclusionArrayFrom](MaterialPropertyBlock.CopyProbeOcclusionArrayFrom.html)|
This function copies the entire source array into a Vector4 property array
named unity_ProbesOcclusion for use with instanced Shadowmask rendering.  
[CopySHCoefficientArraysFrom](MaterialPropertyBlock.CopySHCoefficientArraysFrom.html)|
This function converts and copies the entire source array into 7 Vector4
property arrays named unity_SHAr, unity_SHAg, unity_SHAb, unity_SHBr,
unity_SHBg, unity_SHBb and unity_SHC for use with instanced light probe
rendering.  
[GetColor](MaterialPropertyBlock.GetColor.html)| Get a color from the property
block.  
[GetFloat](MaterialPropertyBlock.GetFloat.html)| Get a float from the property
block.  
[GetFloatArray](MaterialPropertyBlock.GetFloatArray.html)| Get a float array
from the property block.  
[GetInt](MaterialPropertyBlock.GetInt.html)| This method is deprecated. Use
GetFloat or GetInteger instead.  
[GetInteger](MaterialPropertyBlock.GetInteger.html)| Get an integer from the
property block.  
[GetMatrix](MaterialPropertyBlock.GetMatrix.html)| Get a matrix from the
property block.  
[GetMatrixArray](MaterialPropertyBlock.GetMatrixArray.html)| Get a matrix
array from the property block.  
[GetTexture](MaterialPropertyBlock.GetTexture.html)| Get a texture from the
property block.  
[GetVector](MaterialPropertyBlock.GetVector.html)| Get a vector from the
property block.  
[GetVectorArray](MaterialPropertyBlock.GetVectorArray.html)| Get a vector
array from the property block.  
[HasBuffer](MaterialPropertyBlock.HasBuffer.html)| Checks if
MaterialPropertyBlock has the ComputeBuffer property with the given name or
name ID. To set the property, use SetBuffer.  
[HasColor](MaterialPropertyBlock.HasColor.html)| Checks if
MaterialPropertyBlock has the Color property with the given name or name ID.
To set the property, use SetColor.  
[HasConstantBuffer](MaterialPropertyBlock.HasConstantBuffer.html)| Checks if
MaterialPropertyBlock has the ConstantBuffer property with the given name or
name ID. To set the property, use SetConstantBuffer.  
[HasFloat](MaterialPropertyBlock.HasFloat.html)| Checks if
MaterialPropertyBlock has the Float property with the given name or name ID.
To set the property, use SetFloat.  
[HasInt](MaterialPropertyBlock.HasInt.html)| This method is deprecated. Use
HasFloat or HasInteger instead.  
[HasInteger](MaterialPropertyBlock.HasInteger.html)| Checks if
MaterialPropertyBlock has the Integer property with the given name or name ID.
To set the property, use SetInteger.  
[HasMatrix](MaterialPropertyBlock.HasMatrix.html)| Checks if
MaterialPropertyBlock has the Matrix property with the given name or name ID.
This also works with the Matrix Array property. To set the property, use
SetMatrix.  
[HasProperty](MaterialPropertyBlock.HasProperty.html)| Checks if
MaterialPropertyBlock has the property with the given name or name ID. To set
the property, use one of the Set methods for MaterialPropertyBlock.  
[HasTexture](MaterialPropertyBlock.HasTexture.html)| Checks if
MaterialPropertyBlock has the Texture property with the given name or name ID.
To set the property, use SetTexture.  
[HasVector](MaterialPropertyBlock.HasVector.html)| Checks if
MaterialPropertyBlock has the Vector property with the given name or name ID.
This also works with the Vector Array property. To set the property, use
SetVector.  
[SetBuffer](MaterialPropertyBlock.SetBuffer.html)| Set a buffer property.  
[SetColor](MaterialPropertyBlock.SetColor.html)| Set a color property.  
[SetConstantBuffer](MaterialPropertyBlock.SetConstantBuffer.html)| Sets a
ComputeBuffer or GraphicsBuffer as a named constant buffer for the
MaterialPropertyBlock.  
[SetFloat](MaterialPropertyBlock.SetFloat.html)| Set a float property.  
[SetFloatArray](MaterialPropertyBlock.SetFloatArray.html)| Set a float array
property.  
[SetInt](MaterialPropertyBlock.SetInt.html)| This method is deprecated. Use
SetFloat or SetInteger instead.  
[SetInteger](MaterialPropertyBlock.SetInteger.html)| Adds a property to the
block. If an integer property with the given name already exists, the old
value is replaced.  
[SetMatrix](MaterialPropertyBlock.SetMatrix.html)| Set a matrix property.  
[SetMatrixArray](MaterialPropertyBlock.SetMatrixArray.html)| Set a matrix
array property.  
[SetTexture](MaterialPropertyBlock.SetTexture.html)| Set a texture property.  
[SetVector](MaterialPropertyBlock.SetVector.html)| Set a vector property.  
[SetVectorArray](MaterialPropertyBlock.SetVectorArray.html)| Set a vector
array property.  
  
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

