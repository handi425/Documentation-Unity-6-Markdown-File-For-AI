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

# TextGenerator

class in UnityEngine

/

Implemented
in:[UnityEngine.TextRenderingModule](UnityEngine.TextRenderingModule.html)

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

Class that can be used to generate text for rendering.

Caches vertices, character info, and line info for memory friendlyness.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Font](Font.html) font;
        void Start()
        {
            [TextGenerationSettings](TextGenerationSettings.html) settings = new [TextGenerationSettings](TextGenerationSettings.html)();
            settings.textAnchor = [TextAnchor.MiddleCenter](TextAnchor.MiddleCenter.html);
            settings.color = [Color.red](Color-red.html);
            settings.generationExtents = new [Vector2](Vector2.html)(500.0F, 200.0F);
            settings.pivot = [Vector2.zero](Vector2-zero.html);
            settings.richText = true;
            settings.font = font;
            settings.fontSize = 32;
            settings.fontStyle = [FontStyle.Normal](FontStyle.Normal.html);
            settings.verticalOverflow = [VerticalWrapMode.Overflow](VerticalWrapMode.Overflow.html);
            [TextGenerator](TextGenerator.html) generator = new [TextGenerator](TextGenerator.html)();
            generator.Populate("I am a string", settings);
            [Debug.Log](Debug.Log.html)("I generated: " + generator.vertexCount + " verts!");
        }
    }
    

### Properties

[characterCount](TextGenerator-characterCount.html)| The number of characters
that have been generated.  
---|---  
[characterCountVisible](TextGenerator-characterCountVisible.html)| The number
of characters that have been generated and are included in the visible lines.  
[characters](TextGenerator-characters.html)| Array of generated characters.  
[fontSizeUsedForBestFit](TextGenerator-fontSizeUsedForBestFit.html)| The size
of the font that was found if using best fit mode.  
[lineCount](TextGenerator-lineCount.html)| Number of text lines generated.  
[lines](TextGenerator-lines.html)| Information about each generated text line.  
[rectExtents](TextGenerator-rectExtents.html)| Extents of the generated text
in rect format.  
[vertexCount](TextGenerator-vertexCount.html)| Number of vertices generated.  
[verts](TextGenerator-verts.html)| Array of generated vertices.  
  
### Constructors

[TextGenerator](TextGenerator-ctor.html)| Create a TextGenerator.  
---|---  
  
### Public Methods

[GetCharacters](TextGenerator.GetCharacters.html)| Populate the given List
with UICharInfo.  
---|---  
[GetCharactersArray](TextGenerator.GetCharactersArray.html)| Returns the
current UICharInfo.  
[GetLines](TextGenerator.GetLines.html)| Populate the given list with
UILineInfo.  
[GetLinesArray](TextGenerator.GetLinesArray.html)| Returns the current
UILineInfo.  
[GetPreferredHeight](TextGenerator.GetPreferredHeight.html)| Given a string
and settings, returns the preferred height for a container that would hold
this text.  
[GetPreferredWidth](TextGenerator.GetPreferredWidth.html)| Given a string and
settings, returns the preferred width for a container that would hold this
text.  
[GetVertices](TextGenerator.GetVertices.html)| Populate the given list with
generated Vertices.  
[GetVerticesArray](TextGenerator.GetVerticesArray.html)| Returns the current
UIVertex array.  
[Invalidate](TextGenerator.Invalidate.html)| Mark the text generator as
invalid. This will force a full text generation the next time Populate is
called.  
[Populate](TextGenerator.Populate.html)| Will generate the vertices and other
data for the given string with the given settings.  
[PopulateWithErrors](TextGenerator.PopulateWithErrors.html)| Will generate the
vertices and other data for the given string with the given settings.  
  
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

