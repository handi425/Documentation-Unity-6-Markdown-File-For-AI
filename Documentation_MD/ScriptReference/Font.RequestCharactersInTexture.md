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

#  [Font](Font.html).RequestCharactersInTexture

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

public void RequestCharactersInTexture(string characters, int size = 0,
[FontStyle](FontStyle.html) style = FontStyle.Normal);

### Parameters

characters | The characters which are needed to be in the font texture.  
---|---  
size | The size of the requested characters (the default value of zero will use the font's default size).  
style | The style of the requested characters.  
  
### Description

Request characters to be added to the font texture (dynamic fonts only).

Note: You should only ever need to use this when you want to implement your
own text rendering. Call this function to request Unity to make sure all the
characters in the string `characters` are available in the font's font texture
(and it's `characterInfo` property). This is useful when you want to implement
your own code to render dynamic fonts. You can supply a custom font size and
style for the characters. If `size` is zero (the default), it will use the
default size for that font.  
  
RequestCharactersInTexture may cause the font texture to be regenerated if it
does not have space to add all the requested characters. If the font texture
is regenerated it will only contain characters which have been used using
Font.RequestCharactersInTexture, or using Unity's text rendering functions
during the last frame. So it is advisable to always call
RequestCharactersInTexture for any text on the screen you wish to render using
custom font rendering functions, even if the characters are currently present
in the texture, to make sure they don't get purged during texture rebuild.  
  
Additional resources: [textureRebuilt](Font-textureRebuilt.html),
[GetCharacterInfo](Font.GetCharacterInfo.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class CustomFontMeshGenerator : [MonoBehaviour](MonoBehaviour.html)
    {
        [Font](Font.html) font;
        string str = "Hello World";
        [Mesh](Mesh.html) mesh;  
      
        void OnFontTextureRebuilt([Font](Font.html) changedFont)
        {
            if (changedFont != font)
                return;  
      
            RebuildMesh();
        }  
      
        void RebuildMesh()
        {
            // Generate a mesh for the characters we want to print.
            var vertices = new [Vector3](Vector3.html)[str.Length * 4];
            var triangles = new int[str.Length * 6];
            var uv = new [Vector2](Vector2.html)[str.Length * 4];
            [Vector3](Vector3.html) pos = [Vector3.zero](Vector3-zero.html);
            for (int i = 0; i < str.Length; i++)
            {
                // Get character rendering information from the font
                [CharacterInfo](CharacterInfo.html) ch;
                font.GetCharacterInfo(str[i], out ch);  
      
                vertices[4 * i + 0] = pos + new [Vector3](Vector3.html)(ch.minX, ch.maxY, 0);
                vertices[4 * i + 1] = pos + new [Vector3](Vector3.html)(ch.maxX, ch.maxY, 0);
                vertices[4 * i + 2] = pos + new [Vector3](Vector3.html)(ch.maxX, ch.minY, 0);
                vertices[4 * i + 3] = pos + new [Vector3](Vector3.html)(ch.minX, ch.minY, 0);  
      
                uv[4 * i + 0] = ch.uvTopLeft;
                uv[4 * i + 1] = ch.uvTopRight;
                uv[4 * i + 2] = ch.uvBottomRight;
                uv[4 * i + 3] = ch.uvBottomLeft;  
      
                triangles[6 * i + 0] = 4 * i + 0;
                triangles[6 * i + 1] = 4 * i + 1;
                triangles[6 * i + 2] = 4 * i + 2;  
      
                triangles[6 * i + 3] = 4 * i + 0;
                triangles[6 * i + 4] = 4 * i + 2;
                triangles[6 * i + 5] = 4 * i + 3;  
      
                // Advance character position
                pos += new [Vector3](Vector3.html)(ch.advance, 0, 0);
            }
            mesh.vertices = vertices;
            mesh.triangles = triangles;
            mesh.uv = uv;
        }  
      
        void Start()
        {
            font = [Font.CreateDynamicFontFromOSFont](Font.CreateDynamicFontFromOSFont.html)("Helvetica", 16);
            // Set the rebuild callback so that the mesh is regenerated on font changes.
            [Font.textureRebuilt](Font-textureRebuilt.html) += OnFontTextureRebuilt;  
      
            // [Request](PackageManager.Requests.Request.html) characters.
            font.RequestCharactersInTexture(str);  
      
            // Set up mesh.
            mesh = new [Mesh](Mesh.html)();
            GetComponent<[MeshFilter](MeshFilter.html)>().mesh = mesh;
            GetComponent<[MeshRenderer](MeshRenderer.html)>().material = font.material;  
      
            // Generate font mesh.
            RebuildMesh();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Keep requesting our characters each frame, so Unity will make sure that they stay in the font when regenerating the font texture.
            font.RequestCharactersInTexture(str);
        }  
      
        void OnDestroy()
        {
            [Font.textureRebuilt](Font-textureRebuilt.html) -= OnFontTextureRebuilt;
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

