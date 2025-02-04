[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-generate-2d-visual-content.html)
  * [中文](/cn/current/Manual/UIE-generate-2d-visual-content.html)
  * [日本語](/ja/current/Manual/UIE-generate-2d-visual-content.html)
  * [한국어](/kr/current/Manual/UIE-generate-2d-visual-content.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-generate-2d-visual-content.html)
  * [中文](/cn/current/Manual/UIE-generate-2d-visual-content.html)
  * [日本語](/ja/current/Manual/UIE-generate-2d-visual-content.html)
  * [한국어](/kr/current/Manual/UIE-generate-2d-visual-content.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [UI Renderer](UIE-ui-renderer.html)
  * Generate 2D visual content

[](UIE-ui-renderer.html)

UI Renderer

[](UIE-pie-chart.html)

Create a pie chart in the Editor and runtime UI

# Generate 2D visual content

You use the Mesh API or Vector API to generate 2D visual content onto a visual
element.

You can use the Mesh API to draws custom shapes. The Mesh API is a tool for
advanced users. If you only want to generate simple geometry, use the Vector
API instead. Inspired by [HTML Canvas](https://developer.mozilla.org/en-
US/docs/Web/HTML/Element/canvas), the Vector API draws 2D vector graphics,
such as lines, arcs, and shapes.

## Use the Mesh API

To use the Mesh API, allocate a mesh with the
[`MeshGenerationContext.Allocate`](../ScriptReference/UIElements.MeshGenerationContext.Allocate.html)
method and then fill the vertices and indices. The
[`MeshGenerationContext.Allocate`](../ScriptReference/UIElements.MeshGenerationContext.Allocate.html)
method allocates and draws the specified number of vertices and indices
required to express geometry for drawing the content of a visual element. For
details on geometry generation conventions, see
[Vertex.position](../ScriptReference/UIElements.Vertex-position.html).

The following code snippet generates a single quad. It allocates vertices and
indices, and provides coordinates in a clockwise direction:

    
    
    class QuadMeshElement : VisualElement
    {
        public Color color = Color.red;
    
        public QuadMeshElement()
        {
            generateVisualContent += OnGenerateVisualContent;
        }
    
        void OnGenerateVisualContent(MeshGenerationContext mgc)
        {
            var mesh = mgc.Allocate(4, 6);
    
            var p0 = Vector2.zero;
            var p1 = new Vector2(layout.width, 0);
            var p2 = new Vector2(layout.width, layout.height);
            var p3 = new Vector2(0, layout.height);
    
            mesh.SetNextVertex(new Vertex() { position = new Vector3(p0.x, p0.y, Vertex.nearZ), tint = color });
            mesh.SetNextVertex(new Vertex() { position = new Vector3(p1.x, p1.y, Vertex.nearZ), tint = color });
            mesh.SetNextVertex(new Vertex() { position = new Vector3(p2.x, p2.y, Vertex.nearZ), tint = color });
            mesh.SetNextVertex(new Vertex() { position = new Vector3(p3.x, p3.y, Vertex.nearZ), tint = color });
    
            mesh.SetNextIndex(0);
            mesh.SetNextIndex(1);
            mesh.SetNextIndex(2);
            mesh.SetNextIndex(0);
            mesh.SetNextIndex(2);
            mesh.SetNextIndex(3);
        }
    }
    

## Use the Vector API

To use the Vector API, access the
[`Painter2D`](../ScriptReference/UIElements.Painter2D.html) object from the
[`MeshGenerationContext`](../ScriptReference/UIElements.MeshGenerationContext.html)
and generate paths with it. You can then use
[`Stroke`](../ScriptReference/UIElements.Painter2D.Stroke.html) to draw lines
or [`Fill`](../ScriptReference/UIElements.Painter2D.Fill.html) to draw shapes.

To build paths, you issue commands that move a kind of “virtual pen.” For
example, to generate the same quad in the Mesh API example, move the “pen” to
the first position, and chain lines together. After the path is done, use
[`Fill`](../ScriptReference/UIElements.Painter2D.Fill.html) to build the
shape.

    
    
    class QuadVectorElement : VisualElement
    {
        public Color color = Color.red;
    
        public QuadVectorElement()
        {
            generateVisualContent += OnGenerateVisualContent;
        }
    
        void OnGenerateVisualContent(MeshGenerationContext mgc)
        {
            var p0 = Vector2.zero;
            var p1 = new Vector2(layout.width, 0);
            var p2 = new Vector2(layout.width, layout.height);
            var p3 = new Vector2(0, layout.height);
    
            var painter2D = mgc.painter2D;
    
            painter2D.fillColor = color;
    
            painter2D.BeginPath();
            painter2D.MoveTo(p0);
            painter2D.LineTo(p1);
            painter2D.LineTo(p2);
            painter2D.LineTo(p3);
            painter2D.ClosePath();
            painter2D.Fill();
        }
    }
    

### Line

The [`LineTo`](../ScriptReference/UIElements.Painter2D.LineTo.html) method
generates a straight line from the current pen position to the provided one.
Before you draw lines, define properties, such as the stroke color, the line
width, the joins, and caps.

When you draw lines, the properties of
[`LineJoin`](../ScriptReference/UIElements.LineJoin.html) and
[`LineCap`](../ScriptReference/UIElements.LineCap.html) control the styles of
line joins and caps.

The following image illustrates the different styles of line caps and joins:

![Different styles of line caps and joins](../uploads/Main/uitk/line-caps-
joins.png) Different styles of line caps and joins

The following code snippet draws a zigzag line:

![A zigzag line](../uploads/Main/uitk/linto.png) A zigzag line

    
    
    painter2D.lineWidth = 10.0f;
    painter2D.strokeColor = Color.white;
    painter2D.lineJoin = LineJoin.Round;
    painter2D.lineCap = LineCap.Round;
    
    painter2D.BeginPath();
    painter2D.MoveTo(new Vector2(100, 100));
    painter2D.LineTo(new Vector2(120, 120));
    painter2D.LineTo(new Vector2(140, 100));
    painter2D.LineTo(new Vector2(160, 120));
    painter2D.LineTo(new Vector2(180, 100));
    painter2D.LineTo(new Vector2(200, 120));
    painter2D.LineTo(new Vector2(220, 100));
    painter2D.Stroke();
    

### Arc

You can use the following methods to draw arcs:

  * The [`Arc`](../ScriptReference/UIElements.Painter2D.Arc.html) method generates an arc from the provided arc center, the radius, and the starting and ending angles.
  * The [`ArcTo`](../ScriptReference/UIElements.Painter2D.ArcTo.html) method generates an arc between two straight segments.

The following code snippet uses `Arc` to draws a sector with a border:

![A sector with a border](../uploads/Main/uitk/arc.png) A sector with a border

    
    
    painter2D.lineWidth = 2.0f;
    painter2D.strokeColor = Color.red;
    painter2D.fillColor = Color.blue;
    
    painter2D.BeginPath();
    // Move to the arc center
    painter2D.MoveTo(new Vector2(100, 100));
    
    // Draw the arc, and close the path
    painter2D.Arc(new Vector2(100, 100), 50.0f, 10.0f, 95.0f);
    painter2D.ClosePath();
    
    // Fill and stroke the path
    painter2D.Fill();
    painter2D.Stroke();
    

The following code snippet uses `ArcTo` to draw an arc of the requested radius
in the corner of the lines:

![A line with arc](../uploads/Main/uitk/arc-to.png) A line with arc

    
    
    painter2D.BeginPath();
    painter2D.MoveTo(new Vector2(100, 100));
    painter2D.ArcTo(new Vector2(150, 150), new Vector2(200, 100), 20.0f);
    painter2D.LineTo(new Vector2(200, 100));
    painter2D.Stroke();
    

### Curves

You can use the following methods to draw curves:

  * The [`BezierCurveTo`](../ScriptReference/UIElements.Painter2D.BezierCurveTo.html) method generates a cubic bezier curve by two control points and the final position of the cubic bezier.
  * The [`QuadraticCurveTo`](../ScriptReference/UIElements.Painter2D.QuadraticCurveTo.html) method generates a quadratic bezier curve by a control point and the final position of the quadratic bezier.

The following code snippet uses `BezierCurveTo` to draw a bezier curve:

![A bezier curve](../uploads/Main/uitk/curve.png) A bezier curve

    
    
    painter2D.BeginPath();
    painter2D.MoveTo(new Vector2(100, 100));
    painter2D.BezierCurveTo(new Vector2(150, 150), new Vector2(200, 50), new Vector2(250, 100));
    painter2D.Stroke();
    

The following code snippet uses `QuadraticCurveTo` to draw a quadratic curve:

![A quadratic curve](../uploads/Main/uitk/curve-quadratic.png) A quadratic
curve

    
    
    painter2D.BeginPath();
    painter2D.MoveTo(new Vector2(100, 100));
    painter2D.QuadraticCurveTo(new Vector2(150, 150), new Vector2(250, 100));
    painter2D.Stroke();
    

### Holes in fills

You can construct paths with holes in them when you do a
[`Fill`](../ScriptReference/UIElements.Painter2D.html). When you call
`MoveTo`, it starts a new sub-path. To create a hole, use the [fill
rule](../ScriptReference/UIElements.FillRule.html) to overlap the various sub-
paths with each other.

The [fill rule](../ScriptReference/UIElements.FillRule.html) determines how to
fill the inside of a shape:

  * `OddEven`: Draw a ray from that point to infinity in any direction and count the number of path segments from the given shape that the ray crosses. If this number is odd, the point is inside; if even, the point is outside.
  * `NonZero`: Draw a ray from that point to infinity in any direction, and then examine the places where a segment of the shape crosses the ray. Start with a count of zero, and add one each time a path segment crosses the ray from left to right. Subtract one each time a path segment crosses the ray from right to left. After you count the crossings, if the result is zero, then the point is outside the path. Otherwise, it’s inside.

The following code snippet creates a rectangle with a diamond shape hole in
it:

![A rectangle shape with a hole in it](../uploads/Main/uitk/hole.png) A
rectangle shape with a hole in it

    
    
    painter2D.BeginPath();
    painter2D.MoveTo(new Vector2(10, 10));
    painter2D.LineTo(new Vector2(300, 10));
    painter2D.LineTo(new Vector2(300, 150));
    painter2D.LineTo(new Vector2(10, 150));
    painter2D.ClosePath();
    
    painter2D.MoveTo(new Vector2(150, 50));
    painter2D.LineTo(new Vector2(175, 75));
    painter2D.LineTo(new Vector2(150, 100));
    painter2D.LineTo(new Vector2(125, 75));
    painter2D.ClosePath();
    
    painter2D.Fill(FillRule.OddEven);
    

## Additional resources

  * [`MeshGenerationContext`](../ScriptReference/UIElements.MeshGenerationContext.html)
  * [`Painter2D`](../ScriptReference/UIElements.Painter2D.html)
  * [Create a pie chart in the Editor and runtime UI](UIE-pie-chart.html)
  * [Use Mesh API to create a radial progress indicator](UIE-radial-progress.html)
  * [Use Vector API to create a radial progress indicator](UIE-radial-progress-use-vector-api.html)

[](UIE-ui-renderer.html)

UI Renderer

[](UIE-pie-chart.html)

Create a pie chart in the Editor and runtime UI

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

